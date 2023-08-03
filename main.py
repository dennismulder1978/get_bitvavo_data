from func import *

coins_list = ['LUNA2']
periods_list = ['5m', '1h', '2h', '3h', '6h', '12h', '1d', '2d']
column_list = ['Date', 'Open', 'High', 'Low', 'Close', 'Vol.']

for coin in coins_list:
    for period in periods_list:
        print(f'{coin}::{period}')
        go_signal, price_list = price_list(symbol=coin, period=period, go=True)
        if go_signal:
            filename = f'{coin}_trade_data__per_{period}__{len(price_list)}_items'
            save_to_file(list_data=price_list, column_list=column_list, file_name=filename)
