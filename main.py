from func import *

period = '5m'
coin = 'ETH'

price_list = price_list(symbol=coin, period=period)
print(show_time(price_list))

column_list = ['Date', 'Open', 'High', 'Low', 'Close', 'Vol.']
filename = f'{coin}_trade_data__per_{period}__ {len(price_list)}_items'
save_to_file(list_data=price_list, column_list=column_list, file_name=filename)
