# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 01:55:01 2019

@author: Jose Chiramel
"""
import pandas as pd
import numpy as np
data = pd.read_csv("http://www.nasdaq.com/screening/companies-by-name.aspx?letter=0&exchan0ge=nasdaq&render=download")
import pandas_datareader as web
import matplotlib.pyplot as plt
from pprint import pprint
from pandas import Series
from scipy.stats import variation
import pandas as pd
import numpy as np
import statsmodels.api as sm
import pandas_datareader as web
import matplotlib.pyplot as plt
import datetime as datetime
from datetime import  timedelta
from sklearn.metrics import mean_squared_error
import math
import boto3
import json
import time

#from datetime import datetime,timedelta
#import quandl as quandl
symbol1=data['Symbol'].tolist()
symbol= np.array(data['Symbol'])
def start1(code,start,end):
    data = web.DataReader(code,"yahoo",start = start ,end = end)
    if len(data) < 1:
        return False
    else:
        return data
ans= 'C'
while not ans=='Q':
    while not ans=='Q':
        try:    
            code ="global"
            code = input(" enter the company symbol: ")
            if code not in symbol:
                raise ValueError
            else:
                break
        except ValueError:
            print("error")
            print("Would you like to continue(C) or quit(Q)?")
            ans=input("Continue...?")

    
    try:
             start_date = input("PLEASE ENTER THE START DATE FOR ANALYSIS(i.e.(%y,%m,%d) 2018/01/01) : ")
             year, month, day = map(int, start_date.split('/'))
             start_date = datetime.datetime(year, month, day)
             end_date = input("PLEASE ENTER THE END DATE FOR ANALYSIS(i.e.(%y,%m,%d) 2018/01/01): ")
             year, month, day = map(int, end_date.split('/'))
             end_date = datetime.datetime(year, month, day)
             df = start1(code,start_date,end_date) 
             if len(df)>1:
                 break
                 
             elif int(start_date) == int(end_date):
                 raise ValueError
             else:
                 raise ValueError
    except ValueError:
             print("date entered invalid")
             print("Would you like to continue or quit?")
             ans=input("Continue...")
             
df=pd.DataFrame(df)            
