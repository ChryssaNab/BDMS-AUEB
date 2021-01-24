# Implementation of the K-Means clustering algorithm on Hadoop

### [**Contents**](#)
1. [Project Description](#descr)
1. [Installing & Configuring Hadoop](#Inst)
2. [Running K-Means on Hadoop](#Run)
3. [Results](#Results)
4. [Team](#Team)
5. [See also](#ext)

### [**Project Description**](#) <a name="descr"></a>

The aim of this project is to implement k-means clustering algorithm on Hadoop using sythetic data as a sample. The project was implemented in the context of the course "Big Data Management Systems" taught by Prof. Damianos Chatziantoniou. A detailed description of the assignment can be found [here](./Proj1_Hadoop_Description.pdf).


<a name="cont"></a>

### [**Installing & Configuring Hadoop**](#) <a name="Inst"></a>


**1.** We assume that Python3 is already installed in the system.

**2.** Install Hadoop on Linux Ubuntu according to the following website: [How to install Hadoop on Ubuntu 18.04 Bionic Beaver Linux](https://linuxconfig.org/how-to-install-hadoop-on-ubuntu-18-04-bionic-beaver-linux)

**3.** Install necessary requirements.
``` shell
$ pip install -r requirements.txt
```

### [**Running K-Means on Hadoop**](#) <a name="Run"></a>

**1.** Clone this repository:

``` shell
$ git clone https://github.com/ChryssaNab/BDMS-AUEB.git
$ cd /BDMS-AUEB/kmeans_mapreduce/src/
```
**2.** Run **generateDataset.py** to create the input data points. 
- In this example, the initial centers that we used are the following: (-100000, -100000), (1, 1), (100000, 100000)
- The rest of the data points were generated around these points following a normal distribution with standard deviation equal to 5.0. 

**3.** Upload data in **HDFS**.

``` shell
$ hdfs dfs -mkdir /kmeans
$ hdfs dfs -put $HADOOP_HOME/localFilePath/data-points.csv /kmeans
```

**4.** Run **kMeansRunner.py** to implement kmeans on Hadoop.

``` python
 $ python3 kMeansRunner.py
 ```
 
### [**Results**](#) <a name="Results"></a>


<img src="https://github.com/ChryssaNab/BDMS-AUEB/blob/master/kmeans_mapreduce/results/results.png" height="470"/>


<img src="https://github.com/ChryssaNab/BDMS-AUEB/blob/master/kmeans_mapreduce/results/results2.png" height="450"/>


<img src="https://github.com/ChryssaNab/BDMS-AUEB/blob/master/kmeans_mapreduce/results/results3.png" height="130"/>

The output of the MapReduce process is also stored on Hadoop under the name part-00000 :
<img src="https://github.com/ChryssaNab/BDMS-AUEB/blob/master/kmeans_mapreduce/results/hdfs_results.png" height = "350"/>


### [**Team**](#) <a name="Team"></a>

- [Zoe Kotti](https://github.com/zkotti)
- [Chryssa Nampouri](https://github.com/ChryssaNab)

### [**See also**](#) <a name="ext"></a>

External resourses:

- [How to install Hadoop on Ubuntu 18.04 Bionic Beaver Linux](https://linuxconfig.org/how-to-install-hadoop-on-ubuntu-18-04-bionic-beaver-linux)
- [Writing An Hadoop MapReduce Program In Python](https://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/)
