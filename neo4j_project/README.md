# Neo4j Project: Relational vs. Graph Databases

### [**Contents**](#) <a name="cont"></a>
1. [Project Description](#descr)
2. [Execution](#Run)
3. [Benchmarking](#Ben)
4. [Team](#Team)
5. [External Resources](#ext) 

---

### [**Project Description**](#) <a name="descr"></a>

In this project, a dataset was employed with the objective of representing it in both the relational and graph models, executing various queries, and evaluating their performance. The steps undertaken are outlined below:

**1.** Go to [Stanford Large Network Dataset Collection](https://snap.stanford.edu/data/#socnets).

**2.** Use the [Pokec dataset in Social Networks category](https://snap.stanford.edu/data/soc-Pokec.html). 

**3.** For each user keep the 'user_id', 'age', and 'gender' attributes.

**4.** Load the data into MySQL and Neo4j systems. 

**5.** Author queries in SQL and Cypher for the following tasks and benchmark the performance on both systems:

- For each user, count his/her friends.
- For each user, count his/her friends of friends.
- For each user, count his/her friends that are over 30.
- For each male user, count how many male and female friends he is having.

The project was implemented in the context of the course "Big Data Management Systems" taught by Prof. Damianos Chatziantoniou. A detailed description of the assignment can be found [here](./Proj3_Neo4j_Description.pdf).

---

### [Execution](#) <a name="Run"></a>

**1.** We assume that MySQL and Neo4j are already installed and configured on the system. 

**2.** Clone this repository: 
``` shell
$ git clone https://github.com/ChryssaNab/BDMS-AUEB.git
$ cd /BDMS-AUEB/neo4j_project/
```

**3.** Download the dataset:

``` shell
neo4j_project$ mkdir dataset
neo4j_project$ cd dataset
neo4j_project/dataset$ wget "https://snap.stanford.edu/data/soc-pokec-profiles.txt.gz"
neo4j_project/dataset$ wget "https://snap.stanford.edu/data/soc-pokec-relationships.txt.gz"
```
**4.** Execute the **convert_tsv_to_csv.py** script to convert the files from tab-separated (TSV) format to comma-separated (CSV) format, while retaining only the ``user_id``, ``age``, and ``gender`` attributes of the profiles:

``` shell
 $ python convert_tsv_to_csv.py
 ```

**5.** Execute the **write_soc_pokec_mysql.py** script to import the data into MySQL:

``` shell
 $ python write_soc_pokec_mysql.py
 ```
 <img src="https://github.com/ChryssaNab/BDMS-AUEB/blob/master/neo4j_project/configScreenshots/write/count_tables_mysql.PNG" height = "380"/>
 
**6.** Run the following command in the command line to import the data into Neo4j:

``` shell
neo4j_home$ bin/neo4j-admin import
-- id-type INTEGER
-- nodes:User ../import/soc-pokec-profiles-new.csv
-- relationships:HAS_FRIEND ../import/soc-pokec-relationships-new.csv
 ```
 
 <img src="https://github.com/ChryssaNab/BDMS-AUEB/blob/master/neo4j_project/configScreenshots/write/neo4j_soc_pokec.PNG" height = "250"/>

Two examples of the Neo4j graph model are depicted below:

 <img src="https://github.com/ChryssaNab/BDMS-AUEB/blob/master/neo4j_project/configScreenshots/write/neo4j_graph.PNG" height = "400"/>

 <img src="https://github.com/ChryssaNab/BDMS-AUEB/blob/master/neo4j_project/configScreenshots/write/neo4j_graph_2.PNG" height = "400"/>
 
To access Neo4j from a regular browser window, simply enter [http://localhost:7474](http://localhost:7474) and log in with the following credentials: Username: **neo4j**, Password: Your password.


**7.** Execute the **run_queries_mysql.py** script to run the queries in MySQL:
``` shell
 $ python run_queries_mysql.py
 ```
 
 **8.** Execute the **run_queries_neo4j.py** script to run the queries in Neo4j:
``` shell
 $ python run_queries_neo4j.py
 ```

---

### [Benchmarking](#) <a name="Ben"></a>

Queries are executed for 100, 1000, 10,000, 100,000 results, and eventually for the entire dataset. This approach was chosen to observe and compare the performance of MySQL and Neo4j systems across various data sizes.

---

### [Team](#) <a name="Team"></a>

- [Zoe Kotti](https://github.com/zkotti)
- [Chryssa Nampouri](https://github.com/ChryssaNab)

### [**External Resources**](#) <a name="ext"></a>

- [Neo4j-admin Import command line tool](https://neo4j.com/docs/operations-manual/current/tools/neo4j-admin-import/)
