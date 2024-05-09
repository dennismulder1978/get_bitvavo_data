import itertools
from func import *


coins_list = ['doge']
periods_list = ['5m']   # ['5m', '1h', '2h', '6h', '12h', '1d']
column_list = ['Date', 'Open', 'High', 'Low', 'Close', 'Vol.']

for coin, period in itertools.product(coins_list, periods_list):
    print(f'{coin}..{period}:')
    coin_values_list = []
    coin_values_list = price_list(symbol=coin, period=period)

    print(f'Go?: {go_signal}')
    filename = f'{coin}_trade_data__per_{period}__{len(coin_values_list)}_items'
    save_to_file(list_data=coin_values_list,
                column_list=column_list,
                file_name=filename)



print('\n__DONE__')
