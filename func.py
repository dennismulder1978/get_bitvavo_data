from Secret import const
import pandas as pd
from python_bitvavo_api.bitvavo import Bitvavo
from datetime import datetime
from math import ceil


bitvavo = Bitvavo({
    'APIKEY': const.api_key_info,
    'APISECRET': const.api_secret_info,
    'RESTURL': 'https://api.bitvavo.com/v2',
    'WSURL': 'wss://ws.bitvavo.com/v2/',
    'ACCESSWINDOW': 10000,
    'DEBUGGING': False
})


def cohort_creator(period: str= '1d'):
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
    print(f'    Number of candle cohorts: {len(time_list)}..')
    return time_list

def price_list(symbol: str = 'ETH', period: str = '1d', go: bool=True):
    pair = str.upper(symbol) + '-EUR'   # determine pair

    time_list = cohort_creator(period=period)
    datetime_list = []
    coin_values_list = []

    try:
        print('    Start trying to get prices...', end="")
        for i in range(0, len(time_list)):
            print(f' {i + 1}', end="")
            resp = bitvavo.candles(pair, period, {'limit': 1000, 'end': time_list[i]})
            for each in resp:
                each[0] = int(each[0]/1000)
                if i > 0:
                    if each[0] not in datetime_list:
                        coin_values_list.append(each)
                else:
                    coin_values_list.append(each)
                datetime_list.append(each[0])
    except Exception as e:
        print(e)
        go = False
    print('....Done..')
    return go, coin_values_list


def save_to_file(list_data: list, column_list: list, file_name: str = 'file'):
    df = pd.DataFrame(list_data)
    path = './results/'
    name_of_file = path + file_name + f'__created_{datetime.now().strftime("%d-%b-%Y_%H-%M")}.csv'
    df.to_csv(name_of_file, index=False, header=column_list)
    print(f'    File saved. {name_of_file}..')
    return name_of_file + ' saved.'
