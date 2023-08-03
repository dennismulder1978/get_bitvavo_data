from Secret import const
import numpy as np
import pandas as pd
from python_bitvavo_api.bitvavo import Bitvavo
from datetime import datetime
from math import ceil


bitvavo = Bitvavo({
    'APIKEY': const.api_key,
    'APISECRET': const.api_secret,
    'RESTURL': 'https://api.bitvavo.com/v2',
    'WSURL': 'wss://ws.bitvavo.com/v2/',
    'ACCESSWINDOW': 10000,
    'DEBUGGING': False
})


def price_list(symbol: str = 'ETH', period: str = '1d'):
    pair = str.upper(symbol) + '-EUR'   # determine pair

    # create a list of timestamp dates, between each is a 1000 candles
    now_timestamp_in_milliseconds = ceil(datetime.now().timestamp() * 1000)
    time_list = []
    timer = 1
    if period == '1d':
        timer = 86400000000
    if period == '12h':
        timer = 43200000000
    if period == '6h':
        timer = 21600000000
    if period == '1h':
        timer = 3600000000
    if period == '5m':
        timer = 300000000
    if period == '1m':
        timer = 60000000
    for i in range(0, ceil(133574400000 / timer)):  # 133... is 1546 days = approximately total amount of data available
        x = now_timestamp_in_milliseconds - (i * timer)
        time_list.append(x)
    print(f'Length:{len(time_list)}')

    datetime_list = []
    coin_values_list = []
    for i in range(0, len(time_list)):
        resp = bitvavo.candles(pair, period, {'limit': 1000, 'end': time_list[i]})
        for each in resp:
            each[0] = int(int(each[0])/1000)
            if i > 0:
                if each[0] in datetime_list:
                    print('datetime dubbel!!')
                else:
                    coin_values_list.append(each)
            else:
                coin_values_list.append(each)
            datetime_list.append(each[0])
        print(i)
    return coin_values_list


def show_time(time_list: list):
    new_list = []
    for each in time_list:
        new_list.append(datetime.fromtimestamp(each[0]).strftime("%d-%b-%Y %H:%M:%S"))

    print(f'Time list contains: {len(new_list)} items')
    print(new_list[-1:])
    print(new_list[-2:-1])
    for i in range(2):
        print('.')
    print(new_list[1:2])
    print(new_list[:1])
    print('---*****-**----***------*****---****-------***---**----***-----')
    return 'Success'


def save_to_file(list_data: list, column_list: list, file_name: str = 'file'):
    df = pd.DataFrame(list_data)
    name_of_file = file_name + f'__created_{datetime.now().strftime("%d-%b-%Y")}.csv'
    df.to_csv(name_of_file, index=False, header=column_list)
