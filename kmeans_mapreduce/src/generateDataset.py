#!/usr/bin/env python

"""
generateDataset.py: Generates two csv files;
    1. data-points.csv: the data points that will be used for the
        clustering using the K-Means algorithm
    2. data-points-labels.csv: the data points accompanied by the
        label of the cluster they belong to
By default, our clusters are 3, and the data points are in total
1,200,000.

"""

__author__ = "Zoe Kotti, Chryssa Nampouri"

import numpy as np
import pandas as pd
from sklearn.datasets.samples_generator import make_blobs

# Hard-append initial centroids and number of data points
centroids = [[-100000, -100000], [1, 1], [100000, 100000]]
n_samples = 1200000

fileName_points = "data-points.csv"
fileName_points_labels = "data-points-labels.csv"

# Generate the data points by following normal distribution
X, labels = make_blobs(n_samples=n_samples, centers=centroids,
cluster_std=5.0, n_features=2)
# Round data point coordinates to first digit
X = np.round(X, 1)

points = pd.DataFrame(X)
points_labels = pd.DataFrame(X, labels)
# Write files
points.to_csv(fileName_points, sep=',', index=False, header=False)
points_labels.to_csv(fileName_points_labels, sep=',', header=False)
