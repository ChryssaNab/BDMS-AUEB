#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config
import csv
import pymysql
import time


def write_profiles_mysql(profiles_file):
    host = config.HOST
    port = config.PORT
    username = config.USERNAME
    password = config.PASSWORD
    database = config.DATABASE

    query = "INSERT INTO `profiles` (`user_id`, `gender`, `age`) " \
            "VALUES(%s, %s, %s)"

    try:
        connection = pymysql.connect(host=host, port=port, \
                                    user=username, passwd=password, \
                                    db=database)
        # Prepare Cursor object
        cursor = connection.cursor()
        
        # Execute query
        with open(profiles_file, "r", encoding="utf-8") as profiles:
            csv_reader = csv.reader(profiles, delimiter = "\t")

            for row in csv_reader:
                profile = [None, None, None]
                try:
                    profile[0] = int(row[0])
                except:
                    profile[0] = -1
                try:    
                    profile[1] = int(row[3])
                except:
                    profile[1] = -1
                try:
                    profile[2] = int(row[7])
                except:
                    profile[2] = -1
                cursor.execute(query, profile)
                print(profile)

        connection.commit()

    except Exception as e:
        print(e)
    finally:
        connection.close()


def write_relationships_mysql(relationships_file):
    host = config.HOST
    port = config.PORT
    username = config.USERNAME
    password = config.PASSWORD
    database = config.DATABASE

    query = "INSERT INTO `relationships` (`user_id`, `friend_id`) " \
            "VALUES(%s, %s)"

    try:
        connection = pymysql.connect(host=host, port=port, \
                                    user=username, passwd=password, \
                                    db=database)
        # Prepare Cursor object
        cursor = connection.cursor()

        # Execute query
        with open(relationships_file, "r", encoding="utf-8") as relationships:
            csv_reader = csv.reader(relationships, delimiter = "\t")

            for row in csv_reader:
                relationship = [None, None]
                try:
                    relationship[0] = int(row[0])
                except:
                    relationship[0] = -1
                try:
                    relationship[1] = int(row[1])
                except:
                    relationship[1] = -1
                cursor.execute(query, relationship)
                print(relationship)

        connection.commit()

    except Exception as e:
        print(e)
    finally:
        connection.close()


def main():
    profiles_file = "../dataset/soc-pokec-profiles.csv"
    relationships_file = "../dataset/soc-pokec-relationships.csv"

    start_time = time.time()
    write_profiles_mysql(profiles_file)
    elapsed_time = time.time() - start_time
    print("\nProfiles were inserted to MySQL \
    	in {} seconds.\n".format(elapsed_time))

    start_time = time.time()
    write_relationships_mysql(relationships_file)
    elapsed_time = time.time() - start_time
    print("Relationships were inserted to MySQL \
    	in {} seconds.\n".format(elapsed_time)) 


if __name__ == "__main__":

    main()
