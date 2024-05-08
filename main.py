from func import *

coins_list = ['ETH']
periods_list = ['1h']   # ['5m', '1h', '2h', '6h', '12h', '1d']
column_list = ['Date', 'Open', 'High', 'Low', 'Close', 'Vol.']
go_signal = False

for coin in coins_list:
    for period in periods_list:
        print(f'{coin}..{period}:')
        coin_values_list = []
        go_signal, coin_values_list = price_list(symbol=coin,
                                                 period=period,
                                                 go=True)
        print(f'Go?: {go_signal}')
        if go_signal:
            filename = f'{coin}_trade_data__per_{period}__{len(coin_values_list)}_items'
            save_to_file(list_data=coin_values_list,
                         column_list=column_list,
                         file_name=filename)
print('\n__DONE__')
