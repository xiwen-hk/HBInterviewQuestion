#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 23:52:48 2020

@author: cuixiwen
"""
import pandas as pd



  
def initialize(TechnicalSignal,K30_direction,Kline_1,Capital,perShare,commision):

    # Capital = 100000
    # perShare = 1000
    # commision = 0.0020
    
    #Initialize and prepare a tradeRecord
    TradeRecord = pd.DataFrame(columns=['TradingTime','Buy_Sell','Qty','Action','Commision','openPositionQty','openPositionValue','CapitalRemained'])

    # Find the first Entry Point and stablish a base position here
    for i in range(0,Kline_1.shape[0],1):
        if K30_direction['signal'][i] == "upwards":
            TradingTime = Kline_1.index[i]
            Buy_Sell =  "Buy"
            price = Kline_1['open'][i]
            Qty = perShare/Kline_1['open'][i]
            Commision = commision*perShare
            openPositionQty = perShare/Kline_1['open'][i]
            openPositionValue = perShare/Kline_1['open'][i]*Kline_1['close'][i]
            CapitalRemained= Capital- perShare - commision*perShare
            index = i
            Action = 'Open'
            
            
            TradeRecord = TradeRecord.append(pd.DataFrame({'TradingTime':[TradingTime],'Buy_Sell':[Buy_Sell],'price':[price],'Qty':[Qty],'Action':[Action],'index':[index],'Commision':[Commision],'openPositionQty':[openPositionQty], 'openPositionValue': [openPositionValue],'CapitalRemained': [CapitalRemained]}))
            break   
    
    return TradeRecord
