#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config
import csv
import pymysql
import time


def print_info(query, time, file):
    print()
    print(query)
    print("MySQL: Executed in {} seconds".format(time))
    print("Wrote results to {}".format(file))


def write_results(rows, file, headings):
    with open(file, mode='w', newline='') as output_file:
        writer = csv.writer(output_file, delimiter=',', quotechar='"', \
            quoting=csv.QUOTE_MINIMAL)
        writer.writerow(headings)

        for row in rows:
            writer.writerow(row)


def execute_query(query):
    host = config.HOST
    port = config.PORT
    username =  config.USERNAME
    password = config.PASSWORD
    database = config.DATABASE

    try:
        connection = pymysql.connect(host=host, port=port, \
                                    user=username, passwd=password, \
                                    db=database)
        # Prepare Cursor object
        cursor = connection.cursor()

        cursor.execute(query)
        rows = cursor.fetchall()

        connection.commit()

    except Exception as e:
        print(e)
    finally:
        connection.close()

    return rows


# Query 1: For each user, count his/her friends
def count_friends():
    file = "results/q1/count_friends_mysql.csv"
    headings = ["user", "friends"]

    query = """
        SELECT pro.user_id as USER, COUNT(rel.friend_id) as FRIENDS
        FROM profiles pro
        LEFT JOIN relationships rel
        ON pro.user_id = rel.user_id
        GROUP BY pro.user_id;
    """

    start_time = time.time()
    results = execute_query(query)
    elapsed_time = time.time() - start_time

    write_results(results, file, headings)
    print_info(query, elapsed_time, file)


# Query 2: For each user, count his/her friends of friends
def count_friends_of_friends():
    file = "results/q2/count_friends_of_friends_mysql.csv"
    headings = ["user", "friends_of_friends"]

    query = """
        SELECT pro.user_id as USER, COUNT(rel2.friend_id) 
        as FRIENDS_OF_FRIENDS
        FROM profiles pro
        LEFT JOIN relationships rel1
        ON pro.user_id = rel1.user_id
        LEFT JOIN relationships rel2
        ON rel1.friend_id = rel2.user_id
        WHERE pro.user_id != rel2.friend_id
        GROUP BY pro.user_id;
    """

    start_time = time.time()
    results = execute_query(query)
    elapsed_time = time.time() - start_time

    write_results(results, file, headings)
    print_info(query, elapsed_time, file)


# Query 3: For each user, count his/her friends that are over 30
def count_friends_over_thirty():
    file = "results/q3/count_friends_over_thirty_mysql.csv"
    headings = ["user", "friends_over_thirty"]

    query = """
        SELECT pro.user_id as USER, COUNT(rel.friend_id) 
        as FRIENDS_OVER_THIRTY
        FROM profiles pro
        LEFT JOIN relationships rel
        ON pro.user_id = rel.user_id
        AND (
            SELECT pro.age 
            FROM profiles pro
            WHERE pro.user_id = rel.friend_id AND pro.age > 30)
        GROUP BY pro.user_id;
    """

    start_time = time.time()
    results = execute_query(query)
    elapsed_time = time.time() - start_time

    write_results(results, file, headings)
    print_info(query, elapsed_time, file)


# Query 4: For each male user, count how many male and female friends 
# he is having
def count_male_female_friends():
    file = "results/q4/count_male_female_friends_mysql.csv"
    headings = ["user_male", "friends_male", "friends_female"]

    query = """
        SELECT genders.user_id as USER_MALE, \
        COUNT(CASE WHEN genders.gender = 1 THEN 1 END) as FRIENDS_MALE, \
        COUNT(CASE WHEN genders.gender = 0 THEN 1 END) as FRIENDS_FEMALE
        FROM ( 
            SELECT temp.user_id, pro.gender 
            FROM profiles pro, (
                SELECT pro.user_id, pro.age, rel.friend_id 
                FROM profiles pro
                LEFT JOIN relationships rel
                ON pro.user_id = rel.user_id AND pro.gender = 1) as temp 
            WHERE pro.user_id = temp.friend_id) as genders
        GROUP BY genders.user_id;
    """

    start_time = time.time()
    results = execute_query(query)
    elapsed_time = time.time() - start_time

    write_results(results, file, headings)
    print_info(query, elapsed_time, file)


def main():
    count_friends()
    count_friends_of_friends()
    count_friends_over_thirty()
    count_male_female_friends()


if __name__ == "__main__":

    main()
