from Secret import const
from python_bitvavo_api.bitvavo import Bitvavo
from datetime import datetime

bitvavo = Bitvavo({
    'APIKEY': const.api_key,
    'APISECRET': const.api_secret,
    'RESTURL': 'https://api.bitvavo.com/v2',
    'WSURL': 'wss://ws.bitvavo.com/v2/',
    'ACCESSWINDOW': 10000,
    'DEBUGGING': False
})


def period_punisher():
    # determine UNIX-time in milliseconds last whole hour
    # Create list start and stop UNIX-times per 28 dag periods.
    # 2.419.200.000 milliseconds per period.
    # 26 periods in 2 year time.

    last_hour = datetime(
        int(datetime.now().strftime('%Y')),  # current year
        int(datetime.now().strftime('%m')),  # current month
        int(datetime.now().strftime('%d')),  # current day
        int(datetime.now().strftime('%H')),  # current hour
        0,  # current hour, at 0 minutes, 0 seconds (start last hour)
        0,  # current hour, at 0 minutes, 0 seconds (start last hour)
    )

    # to do: MAP function -2415600000 milliseconds in 26 periods list.
    end = int(last_hour.timestamp()*1000)  # converted to milliseconds UNIX-time
    return end


def price_list(symbol: str):
    # Hourly price per pair in periods of 28 days.
    # 24 hours per day, 28 days per period (4 weeks)= 672 hours per period
    pair = str.upper(symbol) + '-EUR'
    resp = bitvavo.candles(pair, '1h', {'limit': 672})
    print(f'{pair} start: {resp[0][0]}')
    print(f'{pair} end: {resp[671][0]}')
    print(f'{pair} delta = {resp[0][0]-resp[671][0]}')

    return [float(resp[x][4]) for x in range(0, len(resp))]
