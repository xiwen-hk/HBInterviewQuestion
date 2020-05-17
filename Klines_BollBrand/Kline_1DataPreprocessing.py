#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 22:25:06 2020

@author: cuixiwen
"""
import time
import datetime
from datetime import timedelta

#convert datetime to next 30minute standard:eg 7:24 to 7：30
def get_hourly_chime(dt, step=0):
    mintue = dt.minute
    deltaMintue = mintue%30
    td = timedelta(days=0, seconds=dt.second, microseconds=dt.microsecond, milliseconds=0, minutes=deltaMintue, hours=-step, weeks=0)
    new_dt = dt - td
    
    return new_dt

def Kline1_preprocessing(Kline_1):
    #截取整半点 
    endTime = get_hourly_chime(Kline_1['datetime'][0])
    startTime = get_hourly_chime(Kline_1['datetime'][Kline_1.shape[0]-1],0.5)

    Kline_1 = Kline_1[Kline_1['datetime']>=startTime ]
    Kline_1 =  Kline_1[Kline_1['datetime']<=endTime]
    
    #sort and order by datetime
    Kline_1.sort_values('datetime',inplace =True,ignore_index = True)
    return Kline_1
