#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import time


def convert_profiles(profiles_file, profiles_file_new):
    with open(profiles_file_new, "w", newline="") as file:
        writer = csv.writer(file, delimiter=",")

        writer.writerow(["userId:ID(User)", "gender:INT", "age:INT"])

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

                writer.writerow(profile)


def convert_relationships(relationships_file, relationships_file_new):
    with open(relationships_file_new, "w", newline="") as file:
        writer = csv.writer(file, delimiter=",")

        writer.writerow([":START_ID(User)", ":END_ID(User)"])

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

                writer.writerow(relationship)


def main():
    profiles_file = "../dataset/soc-pokec-profiles.csv"
    profiles_file_new = "../dataset/soc-pokec-profiles-new.csv"
    relationships_file = "../dataset/soc-pokec-relationships.csv"
    relationships_file_new = "../dataset/soc-pokec-relationships-new.csv"

    start_time = time.time()
    convert_profiles(profiles_file, profiles_file_new)
    elapsed_time_profiles = time.time() - start_time

    start_time = time.time()
    convert_relationships(relationships_file, relationships_file_new)
    elapsed_time_relationships = time.time() - start_time

    print("Conversion of profiles from tsv to csv \
    	took {} seconds.".format(elapsed_time_profiles))
    print("Conversion of relationships from tsv to csv \
    	took {} seconds.".format(elapsed_time_relationships))


if __name__ == "__main__":

    main()
