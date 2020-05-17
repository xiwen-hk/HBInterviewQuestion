#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 00:03:40 2020

@author: cuixiwen
"""

"""
TradingRules:

In upwards direction: 

(1) 如果空仓：那我们就继续开一个底仓

(2) 如果四个技术指标全部是false或者没有capital可以使用了：持仓观察：stay and hold

(3) 如果低于了Boll_bottom，适当加仓。

(4) 如果高于了Boll_up, 清仓获利。（其实也可以换成减仓 我认为均可 我可以尝试下）

(5) 如果上涨穿过MA_5线：证明上涨势头明显，适当加仓。

(6) 如果下跌穿过MA_5线：证明上涨势头减弱，适当减仓。


如果趋势变为downwards,立刻清仓
"""

import pandas as pd
def TradingProcess(TradeRecord,Kline_1,TechnicalSignal,K30_direction,perShare,commision):
    #start from Open point's next minute
    index = int(TradeRecord['index'][0])+1
    
    for i in range(index,Kline_1.shape[0],1):
        #check from Technical Signal
        if K30_direction['signal'][i] =="upwards":
            if TradeRecord['openPositionQty'][TradeRecord.shape[0]-1] == 0:
                TradingTime = Kline_1.index[i]
                Buy_Sell =  "Buy"
                #perShare = 1000
                price = Kline_1['open'][i]
                Qty = perShare/Kline_1['open'][i]
                Commision = commision * perShare
                openPositionQty = perShare/Kline_1['open'][i]
                openPositionValue = perShare/Kline_1['open'][i]*Kline_1['close'][i]
                CapitalRemained= TradeRecord['CapitalRemained'][TradeRecord.shape[0]-1] - perShare - Commision
                index = i
                Action = 'Open'
            
            
                TradeRecord = TradeRecord.append(pd.DataFrame({'TradingTime':[TradingTime],'Buy_Sell':[Buy_Sell],'price':[price],'Qty':[Qty],'Action':[Action],'index':[index],'Commision':[Commision],'openPositionQty':[openPositionQty], 'openPositionValue': [openPositionValue],'CapitalRemained': [CapitalRemained]}),ignore_index=True)
            elif ((TechnicalSignal['lessThanBoll_Bottom'][i] ==False) and (TechnicalSignal['biggerThanBoll_Top'][i] ==False) and (TechnicalSignal['UpThroughMA_5'][i] ==False) and (TechnicalSignal['DownThroughMA_5'][i] ==False)) or (TradeRecord['CapitalRemained'][TradeRecord.shape[0]-1]<=1000):
                #hold and stay 
                #print("Hold and stay")
                continue
            elif TechnicalSignal['lessThanBoll_Bottom'][i] ==True:
                #Increase Position
                TradingTime = Kline_1.index[i]
                Buy_Sell =  "Buy"
                price = Kline_1['open'][i]
                Qty = perShare/Kline_1['open'][i]
                Commision = commision*Qty*price
                openPositionQty = perShare/Kline_1['open'][i] + TradeRecord['openPositionQty'][TradeRecord.shape[0]-1]
                openPositionValue = openPositionQty*Kline_1['close'][i]
                CapitalRemained= TradeRecord['CapitalRemained'][TradeRecord.shape[0]-1] -perShare - Commision
                index = i
                Action = 'Boll_Bottom Increase Position'
                #print("Boll_Bottom Increase Position")
                
                TradeRecord = TradeRecord.append(pd.DataFrame({'TradingTime':[TradingTime],'Buy_Sell':[Buy_Sell],'price':[price],'Qty':[Qty],'Action':[Action],'index':[index],'Commision':[Commision],'openPositionQty':[openPositionQty], 'openPositionValue': [openPositionValue],'CapitalRemained': [CapitalRemained]}),ignore_index = True)
            elif TechnicalSignal['biggerThanBoll_Top'][i] ==True:
                #close position- Take profit
                TradingTime = Kline_1.index[i]
                Buy_Sell =  "Sell"
                price = Kline_1['open'][i]
                Qty = TradeRecord['openPositionQty'][TradeRecord.shape[0]-1]
                Commision = commision*Qty*price
                openPositionQty = 0
                openPositionValue = 0
                CapitalRemained= TradeRecord['CapitalRemained'][TradeRecord.shape[0]-1] +Qty*price - Commision
                index = i
                Action = 'Boll_Up_Close'
                #print("close position- sell all Lock profit")
                
                TradeRecord = TradeRecord.append(pd.DataFrame({'TradingTime':[TradingTime],'Buy_Sell':[Buy_Sell],'price':[price],'Qty':[Qty],'Action':[Action],'index':[index],'Commision':[Commision],'openPositionQty':[openPositionQty], 'openPositionValue': [openPositionValue],'CapitalRemained': [CapitalRemained]}),ignore_index = True)
            elif TechnicalSignal['UpThroughMA_5'][i] ==True:
                # Increase position
                TradingTime = Kline_1.index[i]
                Buy_Sell =  "Buy"
                price = Kline_1['open'][i]
                Qty = perShare/Kline_1['open'][i]
                Commision = commision*Qty*price
                openPositionQty = perShare/Kline_1['open'][i] + TradeRecord['openPositionQty'][TradeRecord.shape[0]-1]
                openPositionValue = openPositionQty*Kline_1['close'][i]
                CapitalRemained= TradeRecord['CapitalRemained'][TradeRecord.shape[0]-1] -perShare - Commision
                index = i
                Action = 'Increase Position'
                #print("Increase position")
                
                TradeRecord = TradeRecord.append(pd.DataFrame({'TradingTime':[TradingTime],'Buy_Sell':[Buy_Sell],'price':[price],'Qty':[Qty],'Action':[Action],'index':[index],'Commision':[Commision],'openPositionQty':[openPositionQty], 'openPositionValue': [openPositionValue],'CapitalRemained': [CapitalRemained]}),ignore_index = True)
            elif TechnicalSignal['DownThroughMA_5'][i] ==True:
                #reduce position
                TradingTime = Kline_1.index[i]
                Buy_Sell =  "Sell"
                price = Kline_1['open'][i]
                Qty = perShare/Kline_1['open'][i]
                Commision = commision*Qty*price
                openPositionQty = perShare/Kline_1['open'][i] - Qty
                openPositionValue = openPositionQty*Kline_1['close'][i]
                CapitalRemained= TradeRecord['CapitalRemained'][TradeRecord.shape[0]-1] + perShare - Commision
                index = i
                Action = 'Reduce Position'
                #print("Reduce position")
                
                TradeRecord = TradeRecord.append(pd.DataFrame({'TradingTime':[TradingTime],'Buy_Sell':[Buy_Sell],'price':[price],'Qty':[Qty],'Action':[Action],'index':[index],'Commision':[Commision],'openPositionQty':[openPositionQty], 'openPositionValue': [openPositionValue],'CapitalRemained': [CapitalRemained]}),ignore_index = True)
        elif K30_direction['signal'][i] =="downwards" and TradeRecord['openPositionQty'][TradeRecord.shape[0]-1]>0:
            #print(i)
            #Close Positions
            TradingTime = Kline_1.index[i]
            Buy_Sell =  "Sell"
            price = Kline_1['open'][i]
            Qty = TradeRecord['openPositionQty'][TradeRecord.shape[0]-1]
            Commision = commision*Qty*price
            openPositionQty = 0
            openPositionValue = 0
            CapitalRemained= TradeRecord['CapitalRemained'][TradeRecord.shape[0]-1] + Qty*price - Commision
            index = i
            Action = 'DownwardsClose'
            #print("DownwardsClose")
            
            TradeRecord = TradeRecord.append(pd.DataFrame({'TradingTime':[TradingTime],'Buy_Sell':[Buy_Sell],'price':[price],'Qty':[Qty],'Action':[Action],'index':[index],'Commision':[Commision],'openPositionQty':[openPositionQty], 'openPositionValue': [openPositionValue],'CapitalRemained': [CapitalRemained]}),ignore_index = True)
        
    return TradeRecord

        
          
          
    