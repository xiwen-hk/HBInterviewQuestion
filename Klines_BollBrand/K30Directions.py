#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 23:32:26 2020

@author: cuixiwen
"""

import pandas as pd
import numpy as np
# Using Kline_30 to get Upwards and Downwards Directions
"""
I have doubts here...

I will mark down my thoughts....

(1) I define Upwards in 30 min's Kline as this minutes' low price is higher than 30min's low price before. 
    
    low[t] > low[t-30min]
    
    I have some dounts here about 30minute Kline, should we only consider (7:00-7:30 and 7:30-8:00) or (7:00-7:30 and 7:01-7:31 and ..) ?
    
    I'm Using the first method to calculate the direction.
    
"""



def K30_directions(Kline_1,Kline_5,Kline_30):
    #Kline_30
    #30 minKline上涨趋势 不破上一个低点:以low price来衡量
    Kline_30['30min_lowPriceChange'] = Kline_30['low'] -Kline_30['low'].shift(1)

    #create a K30_direction
    K30_direction = pd.DataFrame(columns = {'Kline_30Change','signal'},index=Kline_1.index)

    #Fill up the column:Kline_30Change which is numeric number
    for index_30,row_30 in Kline_30.iterrows():
        for index_1,row_1 in Kline_1.iterrows():
            if (index_30 ==index_1):
                K30_direction.loc[index_1,'Kline_30Change'] = Kline_30.loc[index_30,'30min_lowPriceChange']
                break
            
    pd.set_option('mode.chained_assignment', None)

    #Fill up the signal according to Kline_30Change
    for i in range(29,K30_direction.shape[0],30):
        for j in range(1,30,1):
            if i+j+1>=K30_direction.shape[0]:
                break
            if K30_direction['Kline_30Change'][i+j] is np.nan:
                K30_direction['signal'][i+j+1] = K30_direction['signal'][i+j]
            elif (K30_direction['Kline_30Change'][i+j] >0):
                K30_direction['signal'][i+j+1] = "upwards"
                K30_direction['signal'][i+j] = K30_direction['signal'][i+j-1]
            elif (K30_direction['Kline_30Change'][i+j] <= 0):
                K30_direction['signal'][i+j+1]= "downwards"
                K30_direction['signal'][i+j] = K30_direction['signal'][i+j-1]
    K30_direction.to_csv("../Results/K30_direction.csv")
    return  K30_direction