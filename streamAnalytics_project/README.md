# Azure Stream Analytics Project

### [**Contents**](#) <a name="cont"></a>
1. [Project Description](#descr)
1. [Azure Configuration](#Inst)
2. [Azure Stream Analytics: Queries](#Run)
3. [Team](#Team)
4. [See also](#ext) 


### [**Project Description**](#) <a name="descr"></a>

In the context of this assignment a set of Reference Data is given that consists of three JSON fles: 

1. **Customer.json:** Personal data about customers who have made transactions. Each customer example is described by the following attributes:
    - *card_number* (integer)
    - *first_name* (string)
    - *last_name* (string)
    - *age*       (integer)
    - *gender*    (string)
    - *area_code* (integer)

2. **Atm.json:** Describes ATMs as:
    - *atm_code* (integer)
    - *area_code* (integer)

3. **Area.json:** Describes areas as:
    - *area_code* (integer)
    - *area_country* (string)
    - *area_city* (string)

The purpose of this project was to process a data stream of ATM transactions and answer stream queries. The schema of the stream is the 
following: (ATMCode, CardNumber, Type, Amount). The project was implemented in the context of the course "Big Data Management Systems" taught by Prof. Damianos Chatziantoniou. A detailed description of the assignment can be found [here](./Proj4_Stream_Analytics.pdf).

### [Azure Configuration](#) <a name="Inst"></a>

In order to execute the above process on Azure Stream Analytics Platform the following steps are required:

&nbsp;&nbsp;&nbsp; **1.** Create an [Azure account](https://azure.microsoft.com/en-us/). \
&nbsp;&nbsp;&nbsp; **2.** Setup an Event Hub. \
&nbsp;&nbsp;&nbsp; **3.** Generate a [Security Access Signature](https://github.com/sandrinodimattia/RedDog/releases). \
&nbsp;&nbsp;&nbsp; **4.** Edit Generator.html and update the CONFIG variables with your security access signature. \
&nbsp;&nbsp;&nbsp;  **5.** Feed the Event Hub with streaming data by using the Generator.html. \
&nbsp;&nbsp;&nbsp;  **6.** Setup a Storage account. \
&nbsp;&nbsp;&nbsp;  **7.** Upload the Reference Data files to your storage account. \
&nbsp;&nbsp;&nbsp;  **8.** Setup a Stream Analytics Job. \
&nbsp;&nbsp;&nbsp;  **9.** Use the Event Hub and the Reference Data Files as Input. \
&nbsp;&nbsp;&nbsp;  **10.** Create a Blob Storage Output. \
&nbsp;&nbsp;&nbsp;  **11.** Run queries. 


### [Azure Stream Analytics: Queries](#) <a name="Run"></a>

After specifying the input source of the streaming data and the output sink for the results, the following queries were expressed in a SQL-like query language (T-SQL) , in order to
be executed on the Azure Platform:

&nbsp;&nbsp;&nbsp; **1.** Show the total 'Amount' of 'Type = 0' transactions at 'ATM Code = 21' of the last 10 minutes. Repeat as new events keep flowing in (use a 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; sliding window). <br/> 
&nbsp;&nbsp;&nbsp; **2.** Show the total 'Amount' of 'Type = 1' transactions at 'ATM Code = 21' of the last hour. Repeat once every hour (use a tumbling window). <br/>
&nbsp;&nbsp;&nbsp; **3.** Show the total 'Amount' of 'Type = 1' transactions at 'ATM Code = 21' of the last hour. Repeat once every 30 minutes (use a hopping 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; window). <br/>
&nbsp;&nbsp;&nbsp; **4.** Show the total 'Amount' of 'Type = 1' transactions per 'ATM Code' of the last one hour (use a sliding window). <br/>
&nbsp;&nbsp;&nbsp; **5.** Show the total 'Amount' of 'Type = 1' transactions per 'Area Code' of the last hour. Repeat once every hour (use a tumbling window). <br/>
&nbsp;&nbsp;&nbsp; **6.** Show the total 'Amount' per ATM's 'City' and Customer's 'Gender' of the last hour. Repeat once every hour (use a tumbling window). <br/>
&nbsp;&nbsp;&nbsp; **7.** Alert (SELECT '1') if a Customer has performed two transactions of 'Type = 1' in a window of an hour (use a sliding window). <br/>
&nbsp;&nbsp;&nbsp; **8.** Alert (SELECT '1') if the 'Area Code' of the ATM of the transaction is not the same as the 'Area Code' of the 'Card Number' (Customer's 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Area Code) - (use a sliding window). 






### [Team](#) <a name="Team"></a>

- [Zoe Kotti](https://github.com/zkotti)
- [Chryssa Nampouri](https://github.com/ChryssaNab)

### [**See also**](#) <a name="ext"></a>

External resources:

- [Microsoft Azure: Stream Analytics Documentation](https://docs.microsoft.com/en-us/azure/stream-analytics/)
