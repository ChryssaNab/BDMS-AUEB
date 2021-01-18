# Neo4j Project: Relational vs. Graph Databases

### [**Contents**](#) <a name="cont"></a>
1. [Project Description](#descr)
2. [Neo4j Implementation](#Run)
3. [Benchmarking](#Ben)
4. [Team](#Team)
5. [See also](#ext) 


### [**Project Description**](#) <a name="descr"></a>

In this project a dataset was provided and the purpose was to represent it in the relational model, in the graph model, to run some queries and to measure performance. The steps
that were followed are the following:

&nbsp;&nbsp; 1. Go to [Stanford Large Network Dataset Collection](https://snap.stanford.edu/data/#socnets).

&nbsp;&nbsp; 2. Use the [Pokec dataset in Social Networks category](https://snap.stanford.edu/data/soc-Pokec.html). 

&nbsp;&nbsp; 3. For each user keep user_id, age and gender. 

&nbsp;&nbsp; 4. Load data in MySQL and Neo4j. 

5. Write queries in sql and Cypher for the following queries and benchmark both:
    - For each user, count his/her friends.
    - For each user, count his/her friends of friends.
    - For each user, count his/her friends that are over 30.
    - For each male user, count how many male and female friends he is having.

The project was implemented in the context of the course "Big Data Management Systems" taught by Prof. Damianos Chatziantoniou. A detailed description of the assignment can be found [here](./Proj3_Neo4j_Description.pdf).


### [Neo4j Implementation](#) <a name="Run"></a>

**1.** We assume that MySQL and Neo4j are already installed and configured in the system. 

**2.** Clone this repository: 
``` shell
$ git clone https://github.com/ChryssaNab/BDMS-AUEB.git
$ cd /BDMS-AUEB/neo4j_project/
```

**3.** Download the data set:

``` shell
neo4j_project$ mkdir dataset
neo4j_project$ cd dataset
neo4j_project/dataset$ wget "https://snap.stanford.edu/data/soc-pokec-profiles.txt.gz"
neo4j_project/dataset$ wget "https://snap.stanford.edu/data/soc-pokec-relationships.txt.gz"
```
**4.** Run **convert_tsv_to_csv.py** to transform the files from tab-separated (TSV) to comma-separated (CSV) and keep only the "user_id", 
"age", "gender" attributes of profiles.

``` shell
 $ python convert_tsv_to_csv.py
 ```


**5.** Run **write_soc_pokec_mysql.py** to import the data into MySQL.

``` shell
 $ python write_soc_pokec_mysql.py
 ```
 <img src="https://github.com/ChryssaNab/BDMS-AUEB/blob/master/neo4j_project/configScreenshots/write/count_tables_mysql.PNG" height = "380"/>
 
**6.** To load the data to Neo4j, the following command was used in terminal:

``` shell
neo4j_home$ bin/neo4j-admin import
-- id-type INTEGER
-- nodes:User ../import/soc-pokec-profiles-new.csv
-- relationships:HAS_FRIEND ../import/soc-pokec-relationships-new.csv
 ```
 
 <img src="https://github.com/ChryssaNab/BDMS-AUEB/blob/master/neo4j_project/configScreenshots/write/neo4j_soc_pokec.PNG" height = "250"/>

Two examples of the Neo4j graph are depicted below:

 <img src="https://github.com/ChryssaNab/BDMS-AUEB/blob/master/neo4j_project/configScreenshots/write/neo4j_graph.PNG" height = "400"/>

 <img src="https://github.com/ChryssaNab/BDMS-AUEB/blob/master/neo4j_project/configScreenshots/write/neo4j_graph_2.PNG" height = "400"/>
 
To access Neo4j from a regular browser window, type [http://localhost:7474](http://localhost:7474) and signing in with Username: **neo4j**, Password: Your password. 


**7.** Run **run_queries_mysql.py** to execute the queries in MySQL.
``` shell
 $ python run_queries_mysql.py
 ```
 
 **8.** Run **run_queries_neo4j.py** to execute the queries in Neo4j.
``` shell
 $ python run_queries_neo4j.py
 ```
### [Benchmarking](#) <a name="Ben"></a>

Queries were executed for 100, 1000, 10,000, 100,000 results, and finally for the entire dataset. This was preferred in order to see and 
compare the performance of MySQL and Neo4j for different data sizes.

### [Team](#) <a name="Team"></a>

- [Zoe Kotti](https://github.com/zkotti)
- [Chryssa Nampouri](https://github.com/ChryssaNab)

### [**See also**](#) <a name="ext"></a>

External resources:

- [Neo4j-admin Import command line tool](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin-import/)
