from Secret import const
from python_bitvavo_api.bitvavo import Bitvavo


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
    resp = bitvavo.candles(pair, '1m', {})
    return [float(resp[x][4]) for x in range(1, len(resp))]
