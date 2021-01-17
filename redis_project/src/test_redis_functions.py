#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis
import redis_functions as rf


def Print_KLStore(current, name):
    print()
    print('----------' + current +' KL Store----------')

    for key in name.keys():
        print(key, name.lrange(key, 0, -1))

def Test_Create_KLStore():
    name1 = redis.Redis(host='localhost', port=6379, db=0)
    name1.flushdb()

    data_source = '../data-sources/Redis_Data_Source.xml'
    query_string = ''
    position1 = 0
    position2 = 1
    direction = 1

    rf.Create_KLStore(name1, data_source, query_string,
        position1, position2, direction)

    current = 'Initial'
    Print_KLStore(current, name1)

    return name1

def Test_Filter_KLStore():
    name1 = Test_Create_KLStore()

    expression = 'element == 87654321'

    rf.Filter_KLStore(name1, expression)

    current = 'Final'
    Print_KLStore(current, name1)

def Test_Apply_KLStore():
    name1 = Test_Create_KLStore()

    rf.Apply_KLStore(name1, rf.func)

    current = 'Final'
    Print_KLStore(current, name1)

def Test_Aggr_KLStore():
    aggregates = ['avg', 'sum', 'count', 'min', 'max']

    for aggr in aggregates:
        print()
        print('Aggregation: ' + aggr)
        name1 = Test_Create_KLStore()

        rf.Aggr_KLStore(name1, aggr)

        current = 'Final'
        Print_KLStore(current, name1)

def Test_LookUp_KLStore():
    name2 = redis.Redis(host='localhost', port=6379, db=1)
    name3 = redis.Redis(host='localhost', port=6379, db=2)

    name2.flushdb()
    name3.flushdb()

    name2.lpush(12, 't12', 't13')
    name2.lpush(18, 't32')
    name2.lpush(56, 't82', 't62', 't71')

    name3.lpush('t11', 120, 67, 98)
    name3.lpush('t12', 68, 139, 65)
    name3.lpush('t13', 55, 12)
    name3.lpush('t32', 22, 13, 2, 6)
    name3.lpush('t71', 4)
    name3.lpush('t82', 100, 0)
    name3.lpush('t99', 45, 89)

    current = 'Initial'
    Print_KLStore(current, name2)

    current = 'Initial'
    Print_KLStore(current, name3)

    rf.LookUp_KLStore(name2, name3)

    current = 'Final'
    Print_KLStore(current, name2)

def Test_ProjSel_KLStore():
    pname1 = redis.Redis(host='localhost', port=6379, db=3)
    pname2 = redis.Redis(host='localhost', port=6379, db=4)
    pname3 = redis.Redis(host='localhost', port=6379, db=5)
    output_name = redis.Redis(host='localhost', port=6379, db=6)

    pname1.flushdb()
    pname2.flushdb()
    pname3.flushdb()
    output_name.flushdb()

    pname1.lpush('t11', 31, 62, 9)
    pname1.lpush('t15', 75, 91)
    pname1.lpush('t22', 55, 12, 112)
    pname1.lpush('t39', 44)
    pname1.lpush('t44', 42, 98)

    pname2.lpush('t11', 12, 6, 95)
    pname2.lpush('t15', 128)
    pname2.lpush('t22', 43)
    pname2.lpush('t32', 39, 77)
    pname2.lpush('t44', 129)

    pname3.lpush('t11', 182)
    pname3.lpush('t16', 7, 9)
    pname3.lpush('t22', 56, 29)
    pname3.lpush('t38', 32, 82)
    pname3.lpush('t44', 66, 121, 22)

    pnames = [pname1, pname2, pname3]

    current = 'Initial'
    Print_KLStore(current, pname1)

    current = 'Initial'
    Print_KLStore(current, pname2)

    current = 'Initial'
    Print_KLStore(current, pname3)

    expression = "##key != 't22' and ##value > 98"

    rf.ProjSel_KLStore(output_name, pnames, expression)

    current = 'Final'
    Print_KLStore(current, output_name)

# Run test functions
Test_Create_KLStore()
#Test_Filter_KLStore()
#Test_Apply_KLStore()
#Test_Aggr_KLStore()
#Test_LookUp_KLStore()
#Test_ProjSel_KLStore()
