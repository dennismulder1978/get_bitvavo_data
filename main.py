from func import *
import pandas as pd
import numpy as np
from datetime import datetime

'''
Save 2 years of hourly coin-market prices per coin. 
'''

coin_list = ['BTC', 'ETH', 'SOL', 'ADA', 'MATIC', 'AVAX', 'SAND']
coin_price_lst = np.array([price_list(each) for each in coin_list])

# safe to file
name = 'CoinPriceData__' + datetime.now().strftime('%d-%m-%Y_%H.%M.%S') + '.csv'
pd.DataFrame.from_records(coin_price_lst, index=coin_list).T.to_csv(name)
