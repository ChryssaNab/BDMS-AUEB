#!/usr/bin/env python

"""
mapper.py: Performs the Map process.

Input: A csv file with the current centroids of the clusters
Process: Reads the data points from HDFS (STDIN), calculates their
    Manhattan distances from the current centroids,
    and appends them to their closest cluster.
Output: For each data point, a key-value set of its cluster (key) and
    the point's coordinates (value) is returned (e.g. 1 [-5.1, 6.8]).
    The key-value sets are sorted by cluster (key).

"""

__author__ = "Zoe Kotti, Chryssa Nampouri"

import sys
import numpy as np

# Read csv file with current centroids
CENTROIDS_FILE = "old-centroids.csv"

with open(CENTROIDS_FILE, "r") as centroidsFile:
    centroidsFile = centroidsFile.readlines()
    centroids = []

    for centroid in centroidsFile:
        centroid = centroid.strip().split(",")
        centroid = [float(centroid[0]), float(centroid[1])]
        centroids.append(centroid)

# Read input with data points from HDFS (STDIN - standard input)
for line in sys.stdin:
    point = line.strip().split(",")
    point = [float(point[0]), float(point[1])]
    distances = [0] * len(centroids)

    for i in range(len(centroids)):
        # Calculate Manhattan distance
        xDistance = abs(point[0] - centroids[i][0])
        yDistance = abs(point[1] - centroids[i][1])
        distances[i] = xDistance + yDistance
    # Find closest centroid index of data point
    cluster = np.argmin(distances)
    # Write data point and its cluster to STDOUT
    print('%s\t%s' % (cluster, point))
