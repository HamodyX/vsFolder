import requests
import freecurrencyapi
import time
client = freecurrencyapi.Client('fca_live_P9ratpsizBi31Itm5QTcI0qvEqUHtnQDuJHBQBBc')
url = 'https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_P9ratpsizBi31Itm5QTcI0qvEqUHtnQDuJHBQBBc'

req = requests.get(url)

stringed = str(client.latest(currencies=[]))

main_input = str(input("enter: "))
if main_input not in stringed:
    print("INVALID")
else:
    print("VALID, CHECK PASSED")