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


def price_list(symbol: str):
    pair = str.upper(symbol) + '-EUR'
    resp = bitvavo.candles(pair, '1h', {})

    new_price_list = []
    print(f"Length list {pair}: {len(resp)}")
    for i in range(1, len(resp)):
        new_price_list.append(float(resp[i][4]))

    return new_price_list


def log(stringer: str, name: str):
    file = f'{name}.csv'
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
