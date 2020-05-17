#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 22:46:25 2020

@author: cuixiwen
"""
import pandas as pd

"""
Now let's consider Boll Brand(Boll_Top, MA_5, Boll_Bottom) 

where 
            
    Boll_top = MA_5 + 2*std

    &

    Boll_bottom = MA_5 - 2*std
"""
def Boll_Brand(Kline_1):

    ma = 5
    BollBrand = pd.DataFrame(columns={'ma_'+str(ma),'boll_top','boll_bottom'},index = Kline_1.index)
    BollBrand['ma_'+str(ma)]=Kline_1.close.rolling(ma).mean()
    BollBrand['boll_top']=BollBrand['ma_'+str(ma)]+ 2 *Kline_1.close.rolling(ma).std()
    BollBrand['boll_bottom']=BollBrand['ma_'+str(ma)]- 2 *Kline_1.close.rolling(ma).std()

    BollBrand.to_csv("../Results/BollBrand.csv")
    return BollBrand

     
        