#make the updates on change, meaning when data is altered/changed, an update to new stat occurs.

import requests
import freecurrencyapi
import time
from datetime import datetime, timedelta

client = freecurrencyapi.Client('fca_live_P9ratpsizBi31Itm5QTcI0qvEqUHtnQDuJHBQBBc')
url = 'https://api.freecurrencyapi.com/v1/historical?apikey=fca_live_P9ratpsizBi31Itm5QTcI0qvEqUHtnQDuJHBQBBc'

req = requests.get(url)

one_day_delay = datetime.now() - timedelta(days=4)

formated = one_day_delay.strftime('%Y-%m-%d')
new_currency = client.historical(date=formated, base_currency="USD",currencies=["SEK"])["data"]

value = new_currency['2024-02-09']['SEK']
print(value)