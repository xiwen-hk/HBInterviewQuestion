#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 22:27:57 2020

@author: cuixiwen
"""

import pandas as pd

def getKline_n(n,Kline_1):
    if n ==5:
        Kline_5 = pd.DataFrame(columns =Kline_1.columns )
        #Using Kline_1 to generate Kline_5 and Kline_30
        for index,row in Kline_1.iterrows():
            #print(index%30)
             if (index % 5 == 0):
                Kline_5 = Kline_5.append(Kline_1.iloc[index], ignore_index=True)
        
        setIndexForKline(Kline_5)
        
        return Kline_5
    elif n ==30:
        Kline_30 = pd.DataFrame(columns =Kline_1.columns )
        for index,row in Kline_1.iterrows():
            #print(index%30)
             if (index % 30 == 0):
                Kline_30 = Kline_30.append(Kline_1.iloc[index], ignore_index=True)
        setIndexForKline(Kline_30)
        return Kline_30
    else:
        columns = Kline_1.columns
        print("Wrong n...We havent consider other Klines besides 5 and 30")
        Kline_x = ([pd.DataFrame({k: [] for k in columns}), None, None])
        #return an empty dateframe
        return Kline_x

def setIndexForKline(Kline):
    Kline.set_index(['datetime'],inplace = True,drop = True)
    return Kline
            