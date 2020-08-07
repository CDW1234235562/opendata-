# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 16:49:51 2020

@author: Kirito
"""

import matplotlib
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd
import re
import math
import os


plt.rcParams['figure.figsize'] = (10, 5)

font = {'family' : 'monospace',
        'weight' : 'bold',
        'size'   : 13}
matplotlib.rc('font', **font)

Typhoons_data = pd.read_csv("pacific.csv")
Typhoons_data = Typhoons_data.iloc[18062:26136]
Typhoons_data = Typhoons_data.replace(-999 , "")

Typhoons_data['Latitude'] = Typhoons_data['Latitude'].str.extract(r'(\d+\.?\d*)',expand = False)

name_list = Typhoons_data['ID'].drop_duplicates(keep='first')



date_index = name_list.index.tolist()


date = Typhoons_data['Date'][date_index]

year_index_list= ['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015']



def yearcounting(date_list):
    count_2000=0
    count_2001=0
    count_2002=0
    count_2003=0
    count_2004=0
    count_2005=0
    count_2006=0
    count_2007=0
    count_2008=0
    count_2009=0
    count_2010=0
    count_2011=0
    count_2012=0
    count_2013=0
    count_2014=0
    count_2015=0

    for v,i in date_list.iteritems():
        if 20000000< i <20010000:
            count_2000 = count_2000+1
        elif 20010000< i <20020000:
            count_2001 = count_2001+1
        elif 20020000< i <20030000:
            count_2002 = count_2002+1
        elif 20030000< i <20040000:
            count_2003 = count_2003+1
        elif 20040000< i <20050000:
            count_2004 = count_2004+1
        elif 20050000< i <20060000:
            count_2005 = count_2005+1
        elif 20060000< i <20070000:
            count_2006 = count_2006+1
        elif 20070000< i <20080000:
            count_2007 = count_2007+1
        elif 20080000< i <20090000:
            count_2008 = count_2008+1
        elif 20090000< i <20100000:
            count_2009 = count_2009+1
        elif 20100000< i <20110000:
            count_2010 = count_2010+1
        elif 20110000< i <20120000:
            count_2011 = count_2011+1
        elif 20120000< i <20130000:
            count_2012 = count_2012+1
        elif 20130000< i <20140000:
            count_2013 = count_2013+1
        elif 20140000< i <20150000:
            count_2014 = count_2014+1
        elif 20150000< i:
            count_2015 = count_2015+1

    year_data = pd.Series([count_2000,
                           count_2001,
                           count_2002,
                           count_2003,
                           count_2004,
                           count_2005,
                           count_2006,
                           count_2007,
                           count_2008,
                           count_2009,
                           count_2010,
                           count_2011,
                           count_2012,
                           count_2013,
                           count_2014,
                           count_2015],index=year_index_list)
    return year_data

def bargraph_draw (X,Y,width,color,xlabel,ylabel,title):
    X=X
    Y=Y
    fig = plt.figure()
    plt.bar(X,Y,width,color=color)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    
    plt.show()
    

year_data=yearcounting(date)

color = '#054E9F'
    
bargraph_draw (year_index_list,year_data,0.8,color,'years','count','How many typhoons are generated each years')




max_wind = Typhoons_data['Maximum Wind']
SuperTY_level= 115#kt/h

max_wind_index = max_wind[max_wind >= SuperTY_level].index.tolist()
SuperTY_list=Typhoons_data['ID'][max_wind_index]
SuperTY_list = SuperTY_list.drop_duplicates(keep='first')
SuperTY_date_list = Typhoons_data['Date'][SuperTY_list.index.tolist()]




SuperTY_year_data = yearcounting(SuperTY_date_list)
color = '#054E9F'
    
bargraph_draw (year_index_list,SuperTY_year_data,0.8,color,'years','count','How many Supertyphoons are generated each years')





life_index_list1 = Typhoons_data['ID'].drop_duplicates(keep='first').index.tolist()
life_index_list2 = Typhoons_data['ID'].drop_duplicates(keep='last').index.tolist()

life_date_list1 = Typhoons_data['Date'][life_index_list1].tolist()
life_date_list2 = Typhoons_data['Date'][life_index_list2].tolist()


lifetime = []

for i in range(len(life_date_list1)):
    life_time = life_date_list2[i]-life_date_list1[i]
    lifetime.append(life_time)


def meantime(time_list):
    mean_time_year = np.mean(np.array(time_list))
    return mean_time_year





count_2000=[]
count_2001=[]
count_2002=[]
count_2003=[]
count_2004=[]
count_2005=[]
count_2006=[]
count_2007=[]
count_2008=[]
count_2009=[]
count_2010=[]
count_2011=[]
count_2012=[]
count_2013=[]
count_2014=[]
count_2015=[]

for i in life_date_list1:
    if 20000000< i <20010000:
        count_2000.append(lifetime[life_date_list1.index(i)])
    elif 20010000< i <20020000:
        count_2001.append(lifetime[life_date_list1.index(i)])
    elif 20020000< i <20030000:
        count_2002.append(lifetime[life_date_list1.index(i)])
    elif 20030000< i <20040000:
        count_2003.append(lifetime[life_date_list1.index(i)])
    elif 20040000< i <20050000:
        count_2004.append(lifetime[life_date_list1.index(i)])
    elif 20050000< i <20060000:
        count_2005.append(lifetime[life_date_list1.index(i)])
    elif 20060000< i <20070000:
        count_2006.append(lifetime[life_date_list1.index(i)])
    elif 20070000< i <20080000:
        count_2007.append(lifetime[life_date_list1.index(i)])
    elif 20080000< i <20090000:
        count_2008.append(lifetime[life_date_list1.index(i)])
    elif 20090000< i <20100000:
        count_2009.append(lifetime[life_date_list1.index(i)])
    elif 20100000< i <20110000:
        count_2010.append(lifetime[life_date_list1.index(i)])
    elif 20110000< i <20120000:
        count_2011.append(lifetime[life_date_list1.index(i)])
    elif 20120000< i <20130000:
        count_2012.append(lifetime[life_date_list1.index(i)])
    elif 20130000< i <20140000:
        count_2013.append(lifetime[life_date_list1.index(i)])
    elif 20140000< i <20150000:
        count_2014.append(lifetime[life_date_list1.index(i)])
    elif 20150000< i:
        count_2015.append(lifetime[life_date_list1.index(i)])




mean_time_year = [meantime(count_2000),meantime(count_2001),meantime(count_2002),
                  meantime(count_2003),meantime(count_2004),meantime(count_2005),
                  meantime(count_2006),meantime(count_2007),meantime(count_2008),
                  meantime(count_2009),meantime(count_2010),meantime(count_2011),
                  meantime(count_2012),meantime(count_2013),meantime(count_2014),
                  meantime(count_2015),]


bargraph_draw (year_index_list,mean_time_year,0.8,color,'years','days','Typhoon_s survival time')


