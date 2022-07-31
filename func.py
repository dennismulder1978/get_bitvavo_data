import numpy as np
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

    last_hour = datetime(
        int(datetime.now().strftime('%Y')),  # current year
        int(datetime.now().strftime('%m')),  # current month
        int(datetime.now().strftime('%d')),  # current day
        int(datetime.now().strftime('%H')),  # current hour
        0,  # current hour, at 0 minutes, 0 seconds (start last hour)
        0,  # current hour, at 0 minutes, 0 seconds (start last hour)
    )

    period_list = []
    timer = int(last_hour.timestamp()*1000)  # epoch time last whole hour in milliseconds
    for i in range(0, 27):  # 26 periods in 2 year time.
        period_list.append(timer)
        timer -= 2419200000  # 2.419.200.000 milliseconds per period (28 days)
    return period_list


def price_list(symbol: str):
    pair = str.upper(symbol) + '-EUR'   # determine pair
    period_list = period_punisher()  # retrieving period_list per 28 days for 2 years
    pair_list = []  # start with an empty list
    for i in range(0, len(period_list)):
        # Hourly price per pair in periods of 28 days.
        # 24 hours per day, 28 days per period (4 weeks)= 672 hours per period

        resp = bitvavo.candles(pair, '1h', {'end': period_list[i], 'limit': 673})
        if len(resp) == 673:
            for j in range(1, len(resp)):
 #               print(f'{i}-{j}: {resp[j][0]}')
                pair_list.append(float(resp[j][4]))
        else:
            for j in range(1, 673):
                pair_list.append(0)

    #         time_list.append(datetime.fromtimestamp(int(resp[j][0] / 1000)))
    # time_list.pop(671)  # because the first item of the first list is absent: the last is doubled. This corrects.
    pair_list.pop(671)  # because the first item of the first list is absent: the last is doubled. This corrects.
    return pair_list
