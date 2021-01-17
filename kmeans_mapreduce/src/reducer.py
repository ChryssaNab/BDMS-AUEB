#!/usr/bin/env python

"""
reducer.py: Performs the Reduce process.

Input: A key-value set of a cluster (key), its partial sum and the number
    of data points related to the particular sum (value);
    this is the output of Combine Process (combiner.py)
Process: Reads Input from HDFS (STDIN) and calculates for each cluster,
    the total sum of all the partial sums of its data points.
    Then for each cluster, the mean value of its data points is computed;
    that's the cluster's new centroid.
Output: The new centroids of the clusters.

"""

__author__ = "Zoe Kotti, Chryssa Nampouri"

import sys
import ast

current_cluster = None
current_partial_sum = []
cluster = None

# Read Input from HDFS (STDIN - standard input)
for line in sys.stdin:
    cluster, partial = line.strip().split('\t', 1)
    partial_sum = ",".join(partial.split(",", 2)[:2]).replace("(", "")
    num_points = partial.split(",", 2)[2].replace(")", "")
    num_points = int(num_points)
    # Convert String representation of list into actual list
    # (e.g. '[-5.8, 3.6]' --> [-5.8, 3.6])
    partial_sum = ast.literal_eval(partial_sum)

    # Input is sorted by cluster (key) and IF-switch is based on this logic
    if current_cluster == cluster:
        current_partial_sum[0] += partial_sum[0]
        current_partial_sum[1] += partial_sum[1]
        current_num_points += num_points
    else:
        if current_cluster:
            # Calculate new centroid coordinates, rounded to first digit
            xCentroid = round(current_partial_sum[0]/current_num_points, 1)
            yCentroid = round(current_partial_sum[1]/current_num_points, 1)
            new_centroid = [xCentroid, yCentroid]
            # Write new centroid to STDOUT
            print('%s\t' % (new_centroid))
        # Initialize/Update variables
        current_partial_sum = partial_sum
        current_num_points = num_points
        current_cluster = cluster

# Make sure last record is also written to STDOUT
if current_cluster == cluster:
    xCentroid = round(current_partial_sum[0]/current_num_points, 1)
    yCentroid = round(current_partial_sum[1]/current_num_points, 1)
    new_centroid = [xCentroid, yCentroid]
    print('%s\t' % (new_centroid))
