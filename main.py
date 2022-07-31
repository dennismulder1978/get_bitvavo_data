from func import *

coin_list = ['BTC', 'ETH', 'ADA', 'MATIC', 'AVAX', 'SOL']
coin_price_list = [[each, price_list(each)] for each in coin_list]

create_csv(coin_price_list)

