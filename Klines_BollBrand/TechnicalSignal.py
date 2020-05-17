#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 23:38:44 2020

@author: cuixiwen
"""
import pandas as pd

"""
Define Technical Signal:
    
(1) Less Than Boll Bottom :

        Open price < last minute's Boll Bottom : Increase Position
        
(2) biggerThanBoll_Top:

        Open Price > last minute's Boll Top : Close Position
        
(3) Up through MA_5: 
        
        increase position
        
(4) DownThroughMA_5: 
        
        Reduce position
"""

def GenerateTechnicalSignal(BollBrand,Kline_1):
    #Define a TechnicalSignal
    TechnicalSignal=pd.DataFrame(columns=['lessThanBoll_Bottom','biggerThanBoll_Top','UpThroughMA_5','DownThroughMA_5'],index = Kline_1.index)
    
    #Fill up the Technical Signal 
    for i in range(6,Kline_1.shape[0]-1,1):
        if Kline_1['open'][i] <BollBrand['boll_bottom'][i-1]:
             TechnicalSignal['lessThanBoll_Bottom'][i] =True
        elif Kline_1['open'][i] >=BollBrand['boll_bottom'][i-1]:
             TechnicalSignal['lessThanBoll_Bottom'][i] =False
        
        if Kline_1['open'][i] >BollBrand['boll_top'][i-1]:
             TechnicalSignal['biggerThanBoll_Top'][i] =True
        elif Kline_1['open'][i] <=BollBrand['boll_top'][i-1]:
             TechnicalSignal['biggerThanBoll_Top'][i] =False
        
        if Kline_1['open'][i] >BollBrand['ma_5'][i-1] and Kline_1['close'][i-1] <=BollBrand['ma_5'][i-1] :
            TechnicalSignal['UpThroughMA_5'][i] =True
            TechnicalSignal['DownThroughMA_5'][i] =False
        elif Kline_1['open'][i] <BollBrand['ma_5'][i-1] and Kline_1['close'][i-1] >=BollBrand['ma_5'][i-1]:
            TechnicalSignal['DownThroughMA_5'][i] =True
            TechnicalSignal['UpThroughMA_5'][i] =False
        else:
            TechnicalSignal['DownThroughMA_5'][i] =False
            TechnicalSignal['UpThroughMA_5'][i] =False
    TechnicalSignal.to_csv("../Results/TechnicalSignal.csv")
    
    return TechnicalSignal
    
    