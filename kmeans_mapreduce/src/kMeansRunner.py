#!/usr/bin/env python

"""
kMeansRunner.py: Implements the K-Means algorithm using
the Map-Combine-Reduce process.

"""

__author__ = "Zoe Kotti, Chryssa Nampouri"

import ast
import random
import subprocess # Requires Python 3

CENTROIDS_FILE = "old-centroids.csv"
INPUT_FILE = "data-points.csv"
# Create a subdirectory "KMeansProject" inside the current directory
# and save the output according to its name in HDFS
OUTPUT_FILE = "KMeansOutput/part-00000"
CENTROIDS = "all-centroids.csv"

class KMeansRunner(object):
    """
    Implements methods needed to support the K-Means algorithm
    and the Map-Combine-Reduce process.
    """

    @staticmethod
    def RetrieveDataPoints(file):
        """Retrieves the data points from a file.
        :param file: A file with the data points
        :return: A list with the data points
        """
        with open(file, "r") as data:
            data = data.readlines()
            dataList = []
            for d in data:
                d = d.strip().split(",")
                d = [float(d[0]), float(d[1])]
                dataList.append(d)
        return dataList

    @staticmethod
    def AddCentroids(centroids):
        """Adds the current centroids to a file that contains all centroids
        from all the iterations of the K-Means algorithm.
        :param centroids: The new centroids resulted from an iteration
            of the K-Means algorithm
        """
        with open(CENTROIDS, "a") as file:
            for centroid in centroids:
                file.write("%s\n" % str([centroid]).strip('[]'))

    def RetrieveCentroids(self, file):
        """Retrieves the current centroids from a file.
        :param self: An instance of the class KMeansRunner
        :param file: The file that contains only the current centroids
        :return: The current centroids in a list
        """
        with open(file, "r") as centroidsFile:
            centroidsFile = centroidsFile.readlines()
            centroids = []
            for centroid in centroidsFile:
                centroid = ast.literal_eval(centroid)
                centroids.append(centroid)
        return centroids

    @staticmethod
    def CheckCentroids(oldCentroids, newCentroids):
        """Checks whether the cluster centroids of the new iteration of the
        K-Means algorithm differ from those resulted from the last one.
        :param oldCentroids: The last centroids
        :param newCentroids: The new centroids
        :return: A boolean value; True if the centroids have changed
            and False if not
        """
        match = False
        if sorted(oldCentroids) == sorted(newCentroids):
            match = True
        return match

    @staticmethod
    def WriteCentroids(centroids):
        """Updates the file that contains the current centroids with
        the new ones, only in case they differ from the current.
        :param centroids: The new centroids
        """
        with open(CENTROIDS_FILE, "w+") as file:
            for centroid in centroids:
                file.write("%s\n" % str([centroid]).strip('[]'))

if __name__ == "__main__":

    instanceKMeans = KMeansRunner()
    # Retrieve the initial data points
    dataPointsList = instanceKMeans.RetrieveDataPoints(INPUT_FILE)
    # Generate the initial centroids of the clusters randomly
    initialCentroids = random.sample(dataPointsList, k=3)
    instanceKMeans.WriteCentroids(initialCentroids)
    instanceKMeans.Addentroids(initialCentroids)

    match = False
    # Run until centroids do not change for two sequential iterations
    while (match == False):
        # Connect with HDFS and run Map-Combine-Reduce process
        # through Hadoop Streaming
        completed = subprocess.run(["/home/hadoop/hadoop-2.8.5/bin/hadoop",
        "jar",
        "/home/hadoop/hadoop-2.8.5/share/hadoop/tools/lib/hadoop-streaming-2.8.5.jar",
        "-file", "mapper.py", "-mapper","mapper.py",
        "-file","combiner.py" ,"-combiner" ,"combiner.py",
        "-file", "reducer.py", "-reducer", "reducer.py",
        "-file", "old-centroids.csv",
        "-input", "/kmeans/data-points.csv",
        "-output","kmeans_output/output"])
        # Copy files from HDFS locally to KMeansProject subdirectory
        # Attention: The user must first create this directory
        # under the directory where all Python files are located
        output = subprocess.run(["/home/hadoop/hadoop-2.8.5/bin/hadoop",
        "fs", "-get", "/user/hadoop/kmeans_output/output/part-00000",
        "KMeansProject/"])

        oldCentroids = instanceKMeans.RetrieveCentroids(CENTROIDS_FILE)
        newCentroids = instanceKMeans.RetrieveCentroids(OUTPUT_FILE)
        oldCentroids= [list(centroid) for centroid in oldCentroids]
        instanceKMeans.AddCentroids(newCentroids)

        match = instanceKMeans.CheckCentroids(oldCentroids, newCentroids)
        # Centroids have changed during two sequential iterations
        if match == False:
            # Update centroids file with the new ones
            instanceKMeans.WriteCentroids(newCentroids)
            # Remove the output from both HDFS and local directory
            # and re-create it in next iteration
            remove_previous_output_hdfs = subprocess.run(["hdfs",
            "dfs", "-rm", "-r",
            "/user/hadoop/kmeans_output/output"])
            remove_previous_output_local = subprocess.run(["rm",
            "-r", "KMeansOutput/part-00000"])
        # Centroids have NOT changed during two sequential iterations
        else:
            remove_previous_output_local = subprocess.run(["rm",
            "-r", "KMeansOutput/part-00000"])
            # Print the final coordinates of the cluster centroids
            print()
            print("The final coordinates of the cluster centroids are:")
            print("------------------------------------------")
            for i in range(len(newCentroids)):
                print("Cluster " + str(i) + ": " + str(newCentroids[i]))
