from Secret import const
from python_bitvavo_api.bitvavo import Bitvavo
import datetime
import os.path

bitvavo = Bitvavo({
    'APIKEY': const.api_key,
    'APISECRET': const.api_secret,
    'RESTURL': 'https://api.bitvavo.com/v2',
    'WSURL': 'wss://ws.bitvavo.com/v2/',
    'ACCESSWINDOW': 10000,
    'DEBUGGING': False
})


def moving_averages_ratio(symbol: str, first: int, second: int, time_type):
    pair = str.upper(symbol) + '-EUR'
    resp = bitvavo.candles(pair, time_type, {})

    first_ma_cum = float(0)
    second_ma_cum = float(0)

    for i in range(1, first + 1):
        first_ma_cum += float(resp[i][4])
    first_ma = first_ma_cum / first
    print(f'{first}({symbol}) = 1e MA: {first_ma}')
    for j in range(1, second + 1):
        second_ma_cum += float(resp[j][4])

    second_ma = second_ma_cum / second
    print(f'{second}({symbol}) = 2e MA: {second_ma}')
    print(f'Ratio({symbol}): {first_ma / second_ma}', end="\n--------------------\n")

    return first_ma / second_ma


def log(stringer: str, name: str):
    file = f'/home/pi/new_RPI_BITV/rasp_bitvavo/{name}.csv'
    text = f'{stringer},{datetime.datetime.now()}\n'
    if os.path.isfile(file):
        with open(file, 'a') as f:
            f.write(text)
            f.close()
    else:
        with open(file, 'w') as g:
            g.write('Action,Pair,Amount,Price,Error,DateTime\n' + text)
            g.close()

    return