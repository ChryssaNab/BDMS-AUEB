# Redis Project: Key-Value Systems

### [**Contents**](#)
1. [Project Description](#descr)
1. [Installing & Configuring Redis](#Inst)
2. [Implementation of the functions in Redis](#Run)
3. [Results](#Results)
4. [Team](#Team)



<a name="Run"></a>
<a name="Results"></a>
<a name="Team"></a>

### [**Project Description**](#) <a name="descr"></a>
A key-value store is a system that manages a collection of ( key,value ) pairs, where key is unique in this universe. Redis - and other systems - 
allow the value to be a single value (e.g. string, number), a set of values, a list of values, a hash, etc.

Assume a collection of (key, list) pairs, i.e. the value is a list of values, namely strings. Assume that key is a string as well. Let's call such a collection 
a Key-List Store (KL Store). This is a special case of a multi-map data structure, where several values are mapped to a key.

**Example of a Key-List Store:**
| Key | List  | 
| :---:   | :-: | 
| 12 | [t12, t67] | 
| 34 | [t87, t12, t98] |
| ... | ... |
| 76 | [t121, t72, t99, t179] | 

The aim of this project is to implement in Python some certain functions/methods that get one or more KL stores and "return" (or update) a KL store.
All these KL stores should exist in Redis. The project was implemented in the context of the course "Big Data Management Systems" taught by Prof. Damianos Chatziantoniou. A detailed description of the assignment can be found [here](./kmeans_mapreduce/Proj1_Hadoop_Description.pdf).


<a name="cont"></a>

### Installing & Configuring Redis <a name="Inst"></a>


**1.** We assume that Python3 is already installed in the system.

**2.** Install Redis on Linux Ubuntu according to the following website: [How To Install and Secure Redis on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-18-04)


``` shell
$ sudo apt install redis-server
$ sudo nano /etc/redis/redis.conf # Inside the file, find the supervised directive that is set to "no" by default and change it to "systemd".
$ sudo systemctl restart redis.service # Restart the Redis service to reflect the changes you made to the configuration file.
``` 

**3.** Install necessary requirements.
``` shell
$ pip install -r requirements.txt
```

### [**Implementation of the functions in Redis**](#)

**1.** Clone this repository:

``` shell
$ git clone https://github.com/ChryssaNab/BDMS-AUEB.git
$ cd /BDMS-AUEB/redis_project/
```
**2.** Modify paths in the XML file in case of MySQL data-source. 
- In this example, we implemented the functions in case of csv, excel and MySQL data-sources and the data we used are the following:

| user_ID |	transaction_ID |
| :---:   | :-: | 
| 0	| 12345678 |
| 0	| 12345679 |
| 1	| 12345670 |
| 2	| 98765432 | 
| 3	| 23456789 |
| 3	| 34567890 |
| 3 |	87654321 |
| 5 |	20134567 |
| 5 |	30124567 |
| 5	| 30124567 |
| 5	| 87654321 |


**3.** Run **test_redis_functions.py** to implement the functions on Redis.

``` python
 $ python3 test_redis_functions.py
 ```
 
### [**Results**](#)

**Test_Create_KLStore()**

<img src="https://github.com/ChryssaNab/BDMS-AUEB/blob/master/redis_project/results/create_KLStore.png"/>

**Test_Filter_KLStore()**

<img src="https://github.com/ChryssaNab/BDMS-AUEB/blob/master/redis_project/results/Filter_KLStore.png"/>


**Test_Apply_KLStore()**

<img src="https://github.com/ChryssaNab/BDMS-AUEB/blob/master/redis_project/results/Apply_KLStore.png"/>


**Test_Aggr_KLStore()**

<img src="https://github.com/ChryssaNab/BDMS-AUEB/blob/master/redis_project/results/Aggr_KLStore_1.png"/>

<img src="https://github.com/ChryssaNab/BDMS-AUEB/blob/master/redis_project/results/Aggr_KLStore_2.png"/>

<img src="https://github.com/ChryssaNab/BDMS-AUEB/blob/master/redis_project/results/Aggr_KLStore_3.png"/>


**Test_LookUp_KLStore()**

<img src="https://github.com/ChryssaNab/BDMS-AUEB/blob/master/redis_project/results/LookUp_KLStore.png"/>

**Test_ProjSel_KLStore()**

<img src="https://github.com/ChryssaNab/BDMS-AUEB/blob/master/redis_project/results/ProjSel_KLStore.png"/>




### [**Team**](#)

- [Zoe Kotti](https://github.com/zkotti)
- [Chryssa Nampouri](https://github.com/ChryssaNab)
