# -*- coding: utf-8 -*-
"""
CIS545 midterm前内容

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
engine = sqlite3.connect('sample')
# Pandas
#a = [{'a': 121, 'b': 14, 'c': 3}, {'a': 121, 'b': 1, 'c': 5}, {'a': 122, 'b': 13, 'c': 2}, {'a': 121, 'b': 15, 'c': 0}]
#a = pd.DataFrame(a)
#print('原始')
#print(a)
##print('ix Selectin Rows')
##print(a.ix[:,0])
#print('selecting row')
#print(a[a['a'] > 121])
#print('selecting columns')
#print(a[['a']])
#print('数a & delete column')
#a_count = a.groupby('a').count().reset_index().rename(columns = {'b':'个数'}).drop(['c'],axis = 1)
#print(a_count)
#print('Drawing')
#a.plot(kind = 'line', x = 'a', y='b',title = 'sb')
#print('groupby以后找a相对应的bc值')
#a_agg = a.groupby('a').agg('min')
#print(a_agg)
#print('排abc大小')
#a_order = a.sort_values(['a', 'b', 'c'], ascending=True)
#print(a_order)
#print('对比')
#print(a.sort_values(['a'], ascending=True))
#print('添加列')
#d1 = [1,2,3,5]
#print(a.assign(e = d1))
#b = [{'a': 12, 'b1': 14, 'c1': 3}, {'a': 5, 'b1': 1, 'c1': 5}, {'a': 122, 'b1': 13, 'c1': 2}, {'a': 121, 'b1': 15, 'c1': 0}]
#b = pd.DataFrame(b)
#print(b)
#print('合并方式1')
#c = a.merge(b, left_on='c',right_on='a',how = 'outer')
#print(c)
#print('合并方式2')
#d = pd.merge(a,b,on = "a")
#print(d)
#print('选固定的一列有nan的那一行')
#e = c[c['c'].isnull()]
#print(e)
##SQL
#a.to_sql('a_table',engine, if_exists='replace', index = False)
#a_sql = pd.read_sql('select * from a_table',engine)
##print(a_sql)
#b.to_sql('b_table',engine, if_exists='replace', index = False)
#b_sql = pd.read_sql('select * from b_table',engine)
##print(b_sql)
#merge_sql = pd.read_sql('select a_table.b, a_table.c, b_table.b1 from a_table JOIN b_table ON a_table.c = b_table.a',engine)
##print(merge_sql)
#count_sql = pd.read_sql('select a, count(*) as Count from a_table group by a',engine)
##print(count_sql)
#index_sql = pd.read_sql('select * from a_table where a=121 and b>1 and c>0',engine)
#print(index_sql)
#r = requests.get("http://www.google.com")
#print(r.status_code)
#r.enconding = r.apparent_encoding
#print(r.text,"\n")
#print(r.headers)
#url = "http://www.baidu.com"
##爬取框架
#def getHTMLText(url):
#    try:
#        r = requests.get(url)
#        r.raise_for_status()
#        r.encoding = r.apparent_encoding
#        return r.text
#    except:
#        return "产生异常"
#a = getHTMLText(url)
#print(a)

##Testing function
#def change(x):
#    x = x + [1,2,3]
#    return x
#
#info = []
#print(change(info))
#print(info)
##找出一个list中最多的数字及其个数
#a = [1,2,1,2,1,4,2,3,1,3,4,5]
#b = {}
#c = []
#for item in a:
#    
#    b[item] = b.get(item,0) + 1
##print(b)
#m = max(b.values())
#for item in b:
#    
#    if b[item] == m:
#        c.append(item)
#print(c[0])












