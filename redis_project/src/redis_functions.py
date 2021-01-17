#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import pymysql
import re
import redis
import xlrd
import xml.etree.ElementTree as ET


# Function 1
def Create_KLStore(name, data_source, query_string, position1,
    position2, direction):
    """
    This function creates in Redis a KL store using a data source
    from an XML file.

    :param name: The KL store to create in Redis
    :param data_source: A csv file, a relational database, or an Excel file
    :param query_string: The index of the worksheet when the source is an
        Excel file, or an SQL statement when the source is a relational
        database
    :param position1, position2: Integer numbers specifying column
        positions
    :param direction: 1 for KL1(D) and 2 for KL2(D)
    """
    # Parse XML file
    root = ET.parse(data_source).getroot()

    for source in root.findall('datasource'):
        type = source.get('type')

        if type == 'csv':
            path_csv = source.find('path').text
            filename_csv = source.find('filename').text
            filepath_csv = path_csv + filename_csv
            delimiter = source.find('delimiter').text
        elif type == 'excel':
            path_excel = source.find('path').text
            filename_excel = source.find('filename').text
            filepath_excel = path_excel + filename_excel
        else:
            username = source.find('dbconnect/username').text
            password = source.find('dbconnect/password').text
            request = source.find('dbconnect/request').text
            database = source.find('dbconnect/database').text

    # Fetch data from csv file
    if type == 'csv':

        with open(filepath_csv, 'r') as csv_file:

            csv_reader = csv.reader(csv_file, delimiter = delimiter)
            # Skip first line with column titles
            next(csv_reader)

            key_list_dict = {}

            unique_pairs_list = []

            # Direction based on user
            if direction == 1:

                for row in csv_reader:
                    user_id = row[position1]
                    transaction_id = row[position2]

                    if [user_id, transaction_id] in unique_pairs_list:
                        continue

                    name.lpush(user_id, transaction_id)

                    unique_pairs_list.append([user_id, transaction_id])

            # Direction based on transaction
            elif direction == 2:

                for row in csv_reader:
                    user_id = row[position1]
                    transaction_id = row[position2]

                    if [transaction_id, user_id] in unique_pairs_list:
                        continue

                    name.lpush(transaction_id, user_id)

                    unique_pairs_list.append([transaction_id, user_id])
    # Fetch data from Excel file
    elif type == 'excel':

        workbook = xlrd.open_workbook(filepath_excel)

        worksheet = workbook.sheet_by_index(query_string)

        unique_pairs_list = []

        if direction == 1:

            for row in range(1, worksheet.nrows):
                user_id = int(worksheet.cell(row, position1).value)
                transaction_id = int(worksheet.cell(row, position2).value)

                if [user_id, transaction_id] in unique_pairs_list:
                    continue

                name.lpush(user_id, transaction_id)

                unique_pairs_list.append([user_id, transaction_id])

        elif direction == 2:

            for row in range(1, worksheet.nrows):
                user_id = int(worksheet.cell(row, position1).value)
                transaction_id = int(worksheet.cell(row, position2).value)

                if [transaction_id, user_id] in unique_pairs_list:
                    continue

                name.lpush(transaction_id, user_id)

                unique_pairs_list.append([transaction_id, user_id])
    # Fetch data from MySQL database
    else:

        host = 'localhost'
        port = 3306
        query_string = 'SELECT user_id, transaction_id FROM transactions'

        try:
            connection = pymysql.connect(host=host, port=port,
                                         user=username, passwd=password,
                                         db=database)
            # Prepare a cursor object
            cursor = connection.cursor()
            # Execute SQL query
            cursor.execute(query_string)
            # Fetch rows
            result = cursor.fetchall()

            unique_pairs_list = []

            if direction == 1:

                for item in result:
                    user_id = int(item[0])
                    transaction_id = int(item[1])

                    if [user_id, transaction_id] in unique_pairs_list:
                        continue

                    name.lpush(user_id, transaction_id)
                    unique_pairs_list.append([user_id, transaction_id])

            elif direction == 2:

                for item in result:
                    user_id = int(item[0])
                    transaction_id = int(item[1])

                    if [transaction_id, user_id] in unique_pairs_list:
                        continue

                    name.lpush(transaction_id, user_id)
                    unique_pairs_list.append([transaction_id, user_id])

        except Exception as e:
            print(e)

        finally:
            connection.close()

# Function 2
def Filter_KLStore(name1, expression):
    """
    This function applies an expression on all elements of all lists of
    a KL store in Redis. If the return value is true, the element remains
    in the list, otherwise it is removed.
    The particular element is mentioned as 'element' in the expression.

    :param name1: A KL store in Redis
    :param expression: A string representing a valid boolean expression
    """
    to_delete_list = []

    for key in name1.keys():
        key = key.decode('utf-8')

        for i in range(0, name1.llen(key)):
            value = name1.lindex(key, i).decode('utf-8')

            if eval(expression.replace('element', value)):
                continue

            to_delete_list.append([key, value])

    for set in to_delete_list:
        name1.lrem(set[0], 0, set[1])

# Function 3
def func(value):
    """
    This function appends the character '3' to the end of a String.

    :param value: The String to modify
    :return: The modified String
    """
    value = value + '3'
    return value

def Apply_KLStore(name1, func):
    """
    This function performs an element-wise operation using a Python
    function.

    :param name1: The name of the KL store in Redis
    :param func: A Python function that transforms the lists of
        the KL store
    """
    for key in name1.keys():
        for i in range(name1.llen(key)):
            value = name1.lrange(key, i, i)
            # Remove 'b' character in front of a string literal
            value = value[0].decode('utf-8').split()

            value[0] = str(value[0])

            newValue = func(value[0])
            # Update value in position i with new value
            name1.lset(key, i, newValue)

# Function 4
def Aggr_KLStore(name1, aggr):
    """
    This function aggregates each list of a KL store according to
    the specified aggregate, updating the list with just one item,
    the result of the aggregation.

    :param name1: A KL store in Redis
    :param aggr: A string that can have one of the values
        'avg/sum/count/min/max'
    """
    for key in name1.keys():
        values = []

        key = key.decode('utf-8')

        for i in range(0, name1.llen(key)):
            values.append(int(name1.lindex(key, i).decode('utf-8')))

        if aggr == 'avg':
            result = round(sum(values)/len(values), 3)
        elif aggr == 'sum':
            result = sum(values)
        elif aggr == 'count':
            result = len(values)
        elif aggr == 'min':
            result = min(values)
        else:
            result = max(values)

        name1.ltrim(key, 0, 0)

        name1.lset(key, 0, result)

# Function 5
def LookUp_KLStore(name2, name3):
    """
    This function performs a lookup for each element of a list.

    :param name2: The name of the first KL store in Redis
    :param name3: The name of the second KL store in Redis
    """
    for key in name2.keys():
        valueSize = name2.llen(key)

        for i in range(valueSize):
            value_name2 = name2.lrange(key, i, i)

            for j in range(name3.llen(value_name2[0])):
                value_name3 = name3.lrange(value_name2[0], j, j)
                # Remove 'b' character in front of a string literal
                value_name3 = value_name3[0].decode('utf-8').split()

                value_name3[0] = str(value_name3[0])

                name2.rpush(key, value_name3[0])

        for k in range(valueSize):
            name2.lpop(key)

# Function 6
def ProjSel_KLStore(output_name, pnames, expression):
    """
    This function performs a join on the common keys of some KL stores,
    and stores them with their values in a new KL store.
    Then it applies a filtering condition for this new KL store,
    based on the key and the contents of the lists involved.

    :param output_name: The name of the KL store that will be created
    :param pnames: The names of the KL stores that will be used for the
        output
    :param expression: A valid Python boolean expression with the following
        convention: Within the expression, key and KL stores involved
        should be prepended by some special symbol(s),
        e.g. "##key <> 't22' and ##age > 20"
    """
    keys_pname1 = pnames[0].keys()

    for key in keys_pname1:
        counter = 1

        for i in range(1, len(pnames)):
            if key in pnames[i].keys():
                counter += 1

        if counter == len(pnames):
            for i in range(len(pnames)):

                for j in range(0, pnames[i].llen(key)):
                    output_name.lpush(key,
                        pnames[i].lindex(key, j).decode('utf-8'))

    expression_list = expression.split()

    key_values = []

    for ex in expression_list:
        ex = ex.replace("'", "")
        if re.search(r'^\W+', ex):
            ex_sub = re.sub(r'^\W+', '', ex)

            if ex_sub == '':
                continue

            key_values.append([ex, ex_sub])

    to_delete_list = []

    for key in output_name.keys():
        key = key.decode('utf-8')

        for i in range(0, output_name.llen(key)):
            value = output_name.lindex(key, i).decode('utf-8')

            expression2 = expression
            expression2 = expression2.replace(key_values[0][0],
                "'" + key + "'")

            expression2 = expression2.replace(key_values[1][0], value)

            if eval(expression2):
                continue

            to_delete_list.append([key, value])

    for set in to_delete_list:
        output_name.lrem(set[0], 0, set[1])
