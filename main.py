from func import *
import pandas as pd
import numpy as np

'''
Safe 2 years of hourly coin-market prices per coin. 
'''

# coin_list = ['BTC', 'ETH', 'SOL', 'ADA', 'MATIC', 'AVAX', 'SAND']
coin_list = ['BTC']
coin_price_lst = np.array([price_list(each) for each in coin_list])
pd.DataFrame.from_records(coin_price_lst, index=coin_list).T.to_csv('name.csv')
print(pd.DataFrame.from_records(coin_price_lst, index=coin_list).T)
