# Redis Project: Key-Value Systems

### [**Contents**](#)
1. [Project Description](#descr)
1. [Installing and Configuring Redis](#Inst)
2. [Implementation of the Functions in Redis](#Run)
3. [Results](#Results)
4. [Team](#Team)

---

### [**Project Description**](#) <a name="descr"></a>
A key-value store is a system that manages a collection of (key, value) pairs, where each key is unique within its scope. Redis, along with other similar systems, allows the value to be a singular entity (such as a string or number), a set of values, a list of values, a hash, and so forth.

Consider a set of (key, list) pairs, where the value comprises a list of strings, with both the key and the elements of the list being strings. We will refer to this collection as a Key-List Store (KL Store). It represents a special case of a multi-map data structure, wherein multiple values are associated with a single key.

**Example of a Key-List Store:**
| Key | List  | 
| :---:   | :-: | 
| 12 | [t12, t67] | 
| 34 | [t87, t12, t98] |
| ... | ... |
| 76 | [t121, t72, t99, t179] | 

The aim of this project is to implement specific functions in Python that take one or more KL Stores as input and either return a new KL Store or update the existing ones. The project was implemented in the context of the course "Big Data Management Systems" taught by Prof. Damianos Chatziantoniou. A detailed description of the assignment can be found [here](./Proj2_Redis_Description.pdf).


<a name="cont"></a>

---
### [Installing and Configuring Redis](#) <a name="Inst"></a>



**1.** We assume that Python3 is already installed on the system.

**2.** Install Redis on Ubuntu according to the following website: [How To Install and Secure Redis on Ubuntu 18.04](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-redis-on-ubuntu-18-04).


``` shell
$ sudo apt install redis-server
$ sudo nano /etc/redis/redis.conf # Inside the file, find the supervised directive that is set to "no" by default and change it to "systemd".
$ sudo systemctl restart redis.service # Restart the Redis service to reflect the changes you made to the configuration file.
``` 

**3.** Install necessary requirements:
``` shell
$ pip install -r requirements.txt
```

---

### [Implementation of the Functions in Redis](#) <a name="Run"></a>

We have implemented the functions for CSV, Excel, and MySQL data-sources, and the datasets we used are as follows:

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

**1.** Clone this repository:

``` shell
$ git clone https://github.com/ChryssaNab/BDMS-AUEB.git
$ cd /BDMS-AUEB/redis_project/
```

**2.** Modify the paths and credentials in the XML configuration file if using a MySQL data-source. You can locate this file at *./data-sources/Redis_Data_Source.xml*. 


**3.** Run **test_redis_functions.py** to deploy the functions on Redis:

``` python
 $ python3 test_redis_functions.py
 ```

---

### [Results](#) <a name="Results"></a>

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

---


### [Team](#) <a name="Team"></a>

- [Zoe Kotti](https://github.com/zkotti)
- [Chryssa Nampouri](https://github.com/ChryssaNab)
