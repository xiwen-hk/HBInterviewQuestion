#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: cuixiwen
"""
import requestData
import Kline_1DataPreprocessing
import getKline

import K30Directions
import BollBrand
import TechnicalSignal

import TradingInitialize
import TradingProcess


if __name__ == "__main__":
    ##Part1 Requesting Kline_1 Kline_5 Kline_30 data and do preprocessing 
    #Get btcusdt 1min 2000 Kline historical data
    symbol = "btcusdt"
    period = "1min"
    size = 2000# upper limit data request is 2000
    
    Capital = 100000
    perShare = 1000
    commision = 0.0020
    
    #Request data and do preprecessing data on Kline_1
    Kline_1 = requestData.GetKLineRecords_Huobi(period, size, symbol)
    
    Kline_1 = Kline_1DataPreprocessing.Kline1_preprocessing(Kline_1)
    
    #Getting Kline_5 and Kline_30 by processing Kline_1
    Kline_5 = getKline.getKline_n(5,Kline_1)
    Kline_30 = getKline.getKline_n(30,Kline_1)
    
    Kline_1 = getKline.setIndexForKline(Kline_1)
    
    
    ##Part2 Generate K30_driection, BollBrand and Technical Signal
    K30_direction = K30Directions.K30_directions(Kline_1,Kline_5,Kline_30)
    
    bollBrand = BollBrand.Boll_Brand(Kline_1)
    
    technicalSignal = TechnicalSignal.GenerateTechnicalSignal(bollBrand,Kline_1)
    
    #Part3 Start Trading
    TradeRecord = TradingInitialize.initialize(technicalSignal,K30_direction,Kline_1,Capital,perShare,commision)
    #TradeRecord is the Result
    TradeRecord = TradingProcess.TradingProcess(TradeRecord,Kline_1,technicalSignal,K30_direction,perShare,commision)
    
    TradeRecord.to_csv("../Results/TradeRecord.csv")
    ###Final Part TradeRecord is the result,could do some anaysis on TradeRecord.
    pnL = ((TradeRecord.tail(1).openPositionValue+TradeRecord.tail(1).CapitalRemained)/Capital -1)*100
    print('PnL is %10.2f%%'%pnL)
    maxDrawDown = (min(TradeRecord.openPositionValue+TradeRecord.CapitalRemained)/Capital -1)*100
    print('maxDrawDown is %10.2f%%'%maxDrawDown)
    
