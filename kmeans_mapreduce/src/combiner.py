#!/usr/bin/env python

"""
combiner.py: Performs the Combine process.

Input: A key-value set of a data point's coordinates (value)
    and its cluster (key); this is the output of Map Process (mapper.py)
Process: Reads Input from HDFS (STDIN) and calculates for each cluster,
    partial sums of its data points in batches.
Output: For each batch of partial sums, a key-value set
    of its cluster (key), its partial sum and the number of data points
    related to the particular sum (value) is returned
    (e.g. 1 ([-5.1, 6.8], 4)).
    The key-value sets are sorted by cluster (key).

"""

__author__ = "Zoe Kotti, Chryssa Nampouri"

import sys
import ast

current_cluster = None
partial_sum = []
cluster = None

# Read Input from HDFS (STDIN - standard input)
for line in sys.stdin:
    cluster, point = line.strip().split('\t', 1)
    # Convert String representation of list into actual list
    # (e.g. '[-5.8, 3.6]' --> [-5.8, 3.6])
    point = ast.literal_eval(point)

    # Input is sorted by cluster (key) and IF-switch is based on this logic
    if current_cluster == cluster:
        partial_sum[0] += point[0]
        partial_sum[1] += point[1]
        num_points += 1
    else:
        if current_cluster:
            # Write cluster, partial sum and number
            # of data points to STDOUT
            print ('%s\t%s' % (current_cluster,
                (partial_sum, num_points)))
        # Initialize/Update variables
        partial_sum = point
        num_points = 1
        current_cluster = cluster

# Make sure last record is also written to STDOUT
if current_cluster == cluster:
    print ('%s\t%s' % (current_cluster, (partial_sum, num_points)))
