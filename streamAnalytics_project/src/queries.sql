1st query:

/*
    Q1: Show the total 'Amount' of 'Type = 0' transactions at 'ATM Code = 21'
    of the last 10 minutes. Repeat as new events keep flowing in (use a sliding window).
*/

SELECT
    sum(CAST([input].[Amount] AS BIGINT)) as Total_Amount, 
    System.Timestamp() AS Event_Time
INTO [output]
FROM
    [input] 
WHERE [input].[Type] = 0 and [input].[ATMCode] = 21
GROUP BY SlidingWindow(minute, 10)


2nd query:

/*
    Q2: Show the total 'Amount' of 'Type = 1' transactions at 'ATM Code = 21'
    of the last hour. Repeat once every hour (use a tumbling window).
*/

SELECT
    sum(CAST([input].[Amount] AS BIGINT)) as Total_Amount, 
    System.Timestamp() AS Time
INTO [output]
FROM
    [input]
WHERE [input].[Type] = 1 and [input].[ATMCode] = 21
GROUP BY TumblingWindow(hour, 1)


3rd query:

/*
    Q3: Show the total 'Amount' of 'Type = 1' transactions at 'ATM Code = 21'
    of the last hour. Repeat once every 30 minutes (use a hopping window).
*/

SELECT
    sum(CAST([input].[Amount] AS BIGINT)) as Total_Amount, 
    System.Timestamp() AS Time
INTO [output]
FROM
    [input]
WHERE [input].[Type] = 1 and [input].[ATMCode] = 21
GROUP BY HoppingWindow(minute, 60, 30)


4th query:

/*
    Q4: Show the total 'Amount' of 'Type = 1' transactions per 'ATM Code'
    of the last one hour (use a sliding window).
*/

SELECT
    [input].[ATMCode],
    sum(CAST([input].[Amount] AS BIGINT)) as Total_Amount, 
    System.Timestamp() AS Time
INTO [output]
FROM
    [input]
WHERE Type = 1
GROUP BY [input].[ATMCode],
         SlidingWindow(hour, 1)


5th query:

/*
    Q5: Show the total 'Amount' of 'Type = 1' transactions per 'Area Code'
    of the last hour. Repeat once every hour (use a tumbling window).
*/

SELECT
    [inputAtm].[area_code],
    sum(CAST([input].[Amount] AS BIGINT)) as Total_Amount, 
    System.Timestamp() AS Time
INTO [output]
FROM
    [input]
INNER JOIN [inputAtm] 
    ON [input].[ATMCode] = [inputAtm].[atm_code] 
WHERE [input].[Type] = 1
GROUP BY [inputAtm].[area_code],
         TumblingWindow(hour, 1)


6th query:

/*
    Q6: Show the total 'Amount' per ATM's 'City' and Customer's 'Gender' 
    of the last hour. Repeat once every hour (use a tumbling window).
*/

SELECT
    [inputArea].[area_city],
    [inputCustomers].[gender],
    sum(CAST([input].[Amount] AS BIGINT)) as Total_Amount, 
    System.Timestamp() AS Time
INTO [output]
FROM
    [input]
INNER JOIN [inputAtm]
    ON [input].[ATMCode] = [inputAtm].[atm_code] 
INNER JOIN [inputArea]
    ON [inputAtm].[area_code] = [inputArea].[area_code]
INNER JOIN [inputCustomers]
    ON [input].[CardNumber] = [inputCustomers].[card_number]
GROUP BY [inputArea].[area_city],
         [inputCustomers].[gender], 
         TumblingWindow(hour, 1)


7th query:

/*
    Q7: Alert (SELECT '1') if a Customer has performed two transactions
    of 'Type = 1' in a window of an hour (use a sliding window).
*/

SELECT
    [inputCustomers].[first_name],
    [inputCustomers].[last_name],
    [input].[CardNumber] AS Card_Number,
    COUNT (*) AS Transactions,
    System.Timestamp AS Time
INTO
    [output]
FROM
    [input]
INNER JOIN [inputCustomers]
    ON [inputCustomers].[card_number] = [input].[CardNumber]
WHERE [input].[Type] = 1
GROUP BY [inputCustomers].[first_name],
         [inputCustomers].[last_name],
         [input].[CardNumber],
         SlidingWindow(hour, 1)
HAVING Transactions = 2


8th query:

/*
    Q8: Alert (SELECT '1') if the 'Area Code' of the ATM of the transaction 
    is not the same as the 'Area Code' of the 'Card Number' 
    (Customer's Area Code) - (use a sliding window).
*/


SELECT
    [inputAtm].[area_code] AS Atm_Area_Code,
    [inputCustomers].[area_code] AS Customer_Area_Code,
    COUNT (*),
    System.Timestamp AS Time
INTO
    [output]
FROM
    [input]
INNER JOIN [inputCustomers]
    ON [inputCustomers].[card_number] = [input].[CardNumber]
INNER JOIN [inputAtm]
    ON [inputAtm].[atm_code] = [input].[ATMCode]
WHERE [inputAtm].[area_code] != [inputCustomers].[area_code]
GROUP BY [inputAtm].[area_code],
         [inputCustomers].[area_code], 
         SlidingWindow(hour, 1)
