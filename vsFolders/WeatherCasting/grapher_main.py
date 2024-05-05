import requests
import freecurrencyapi
import time
from datetime import datetime, timedelta

client = freecurrencyapi.Client('fca_live_P9ratpsizBi31Itm5QTcI0qvEqUHtnQDuJHBQBBc')
url_historical = 'https://api.freecurrencyapi.com/v1/historical?apikey=fca_live_P9ratpsizBi31Itm5QTcI0qvEqUHtnQDuJHBQBBc'
url_latest = 'https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_P9ratpsizBi31Itm5QTcI0qvEqUHtnQDuJHBQBBc'
one_day_delay = datetime.now() - timedelta(days=2)
one_day_delay = one_day_delay.strftime('%Y-%m-%d')
update_time = 1 * 60 # Will replace with user input instead.


req = requests.get(url_latest)

def request():
    if req.status_code == 200:

            mon_currency = str(input("Please Enter 'Base' Currency: ")).upper()
            if mon_currency not in str(client.latest(currencies=[])): #ERROR CONFIGS
                print("INVALID INPUT, PLEASE CHOSE THE CORRECT CURRENCY!")
                return request()
            old_base_currency = client.historical(date=one_day_delay,currencies=["SEK"])['data']
            value = old_base_currency[one_day_delay][mon_currency]
            
            while True:
                new_currency = client.latest(base_currency="USD",currencies=[mon_currency])['data'][mon_currency]
                if new_currency != value: #Shouldn't be any error here :sob:
                    if new_currency > value:
                        print(f"Value Raising! {new_currency}")
                    elif new_currency < value:
                        print(f"Value Decreasing! {new_currency}")
                    value = new_currency
                    print("Updating In 15 Minutes...")
                    time.sleep(update_time)
                else:
                    print(f"Error in fetch, retrying in {update_time / 60}")
                    time.sleep(update_time)

request()

##PROCENTAGE INFO BETWEEN OLD AND NEW VALUE##
##TESTING ONGOING##
#Value Decreasing! 10.510691412