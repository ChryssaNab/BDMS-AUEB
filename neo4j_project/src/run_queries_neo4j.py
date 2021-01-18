#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config
import csv
from py2neo import Graph
import time


def print_info(query, time, file):
    print()
    print(query)
    print("Neo4j: Executed in {} seconds".format(time))
    print("Wrote results to {}".format(file))


def write_results(results, file, headings):
    with open(file, mode='w', newline='') as output_file:
        writer = csv.writer(output_file, delimiter=',', quotechar='"', \
            quoting=csv.QUOTE_MINIMAL)
        writer.writerow(headings)

        for result in results:
            writer.writerow(result)


def execute_query(query, fields):
    password = config.NEO4J_PASSWORD
    graph = Graph(password=password)  
    cursor = graph.run(query)
    results = []

    while cursor.forward():
        new_result = []
        for field in fields:
            new_result.append(cursor.current[field])
        results.append(new_result)

    return results


# Query 1: For each user, count his/her friends
def count_friends():
    file = "results/q1/count_friends_neo4j.csv"
    headings = ["user", "friends"]

    query = """
        MATCH (User)
        OPTIONAL MATCH (User)-[:HAS_FRIEND]->(u)
        RETURN User.userId AS user, COUNT(u) AS friends
        ORDER BY User.userId;
    """

    start_time = time.time()
    results = execute_query(query, headings)
    elapsed_time = time.time() - start_time

    write_results(results, file, headings)
    print_info(query, elapsed_time, file)


# Query 2: For each user, count his/her friends of friends
def count_friends_of_friends():
    file = "results/q2/count_friends_of_friends_neo4j.csv"
    headings = ["user", "friends_of_friends"]

    query = """
        MATCH (User)
        OPTIONAL MATCH (User)-[:HAS_FRIEND*2]->(f)
        WHERE f <> User
        RETURN User.userId AS user, COUNT(f) AS friends_of_friends
        ORDER BY User.userId;
    """

    start_time = time.time()
    results = execute_query(query, headings)
    elapsed_time = time.time() - start_time

    write_results(results, file, headings)
    print_info(query, elapsed_time, file)


# Query 3: For each user, count his/her friends that are over 30
def count_friends_over_thirty():
    file = "results/q3/count_friends_over_thirty_neo4j.csv"
    headings = ["user", "friends_over_thirty"]

    query = """
        MATCH (User)
        OPTIONAL MATCH (User)-[:HAS_FRIEND]->(u)
        WHERE u.age > 30
        RETURN User.userId AS user, COUNT(u) AS friends_over_thirty
        ORDER BY User.userId;
    """

    start_time = time.time()
    results = execute_query(query, headings)
    elapsed_time = time.time() - start_time

    write_results(results, file, headings)
    print_info(query, elapsed_time, file)


# Query 4: For each male user, count how many male and female friends 
# he is having
def count_male_female_friends():
    file = "results/q4/count_male_female_friends_neo4j.csv"
    headings = ["user_male", "friends_male", "friends_female"]

    query = """
        MATCH (User)-[:HAS_FRIEND]->(u)
        WHERE User.gender = 1
        RETURN User.userId AS user_male,
        SUM(CASE WHEN (u.gender = 1) THEN 1 ELSE 0 END) AS friends_male,      
        SUM(CASE WHEN (u.gender = 0) THEN 1 ELSE 0 END) AS friends_female
        ORDER BY User.userId;
    """

    start_time = time.time()
    results = execute_query(query, headings)
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
