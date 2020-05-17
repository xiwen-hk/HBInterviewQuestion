#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 22:02:56 2020

@author: cuixiwen
"""

#Import essential packages
import requests
import pandas as pd
import time
import datetime
from datetime import timedelta

#def a function to using huobi API to get history Kline data and return a dataframe
def GetKLineRecords_Huobi (period, size, symbol):
    BaseUrl = "https://api.huobi.br.com"
    requestMove = "/market/history/kline"
    
    url = BaseUrl + requestMove + '?period=' + period + '&size=' + str(size) +'&symbol=' + symbol
    
    resp = requests.get(url)
    
    resp_json = resp.json()
    df = pd.DataFrame(resp_json['data'])
    df['datetime'] = [datetime.datetime.fromtimestamp(unix_time) for unix_time in df.id ]
    
    return df

#Get current Price
def get_current_price():
    url = 'https://www.huobi.co/-/x/pro/market/overview5?r=ny2seo'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        price_usdt= data['data'][2]['close']
        return price_usdt
    else:
        return 0