import requests
import freecurrencyapi
import time
client = freecurrencyapi.Client('fca_live_P9ratpsizBi31Itm5QTcI0qvEqUHtnQDuJHBQBBc')
url = 'https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_P9ratpsizBi31Itm5QTcI0qvEqUHtnQDuJHBQBBc'

req = requests.get(url)

def request():
    if req.status_code == 200:
        input_prim = str(input("Please Enter 'From' Currency: ")).upper()
        if input_prim not in str(client.latest(currencies=[])):
            print("INVALID INPUT, PLEASE CHOSE THE CORRECT CURRENCY!")
            request()
        try:
            input_value = float(input(f"Enter The Amount In: {input_prim}: "))
        except:
            print("Invalid value")
            request()
        input_scnd = str(input("Please Enter 'To' Currency: ")).upper()
        if input_scnd not in str(client.latest(currencies=[])):
            print("INVALID INPUT, PLEASE CHOSE THE CORRECT CURRENCY!")
            request()
        time.sleep(1)

#client.latest(base_currency='EUR')
        send = client.latest(base_currency=input_prim,currencies=[input_prim])['data'][input_prim]
        recive = client.latest(base_currency=input_prim,currencies=[input_scnd])['data'][input_scnd]

        fixed_prim = round((send * input_value), 2)
        fixed_scnd = round((recive * input_value), 2)

        print(fixed_prim,":", (input_prim)," = ", fixed_scnd,":", (input_scnd))
    else:
        print(f"Error raised, {req.status_code}")

request()

