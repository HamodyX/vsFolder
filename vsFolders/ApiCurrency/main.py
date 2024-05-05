import requests
import freecurrencyapi
import time
client = freecurrencyapi.Client('fca_live_P9ratpsizBi31Itm5QTcI0qvEqUHtnQDuJHBQBBc')
url = 'https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_P9ratpsizBi31Itm5QTcI0qvEqUHtnQDuJHBQBBc'

try:
    req = requests.get(url)
except ValueError:
    print("Uknown error")

def request():
    if req.status_code == 200:
        input_prim = str(input("Please Enter 'From' Currency: ")).upper()
        if input_prim not in str(client.latest(currencies=[])): #ERROR CONFIGS
            print("INVALID INPUT, PLEASE CHOSE THE CORRECT CURRENCY!")
            return request()
        input_value = input(f"Enter The Amount In: {input_prim}: ")
        try: #ERROR CONFIGS
            input_value = float(input_value)
            input_value
        except:
            print("INVALID INPUT, PLEASE CHOSE THE CORRECT VAlUE!")
            return request()
        input_scnd = str(input("Please Enter 'To' Currency: ")).upper()
        if input_scnd not in str(client.latest(currencies=[])): #ERROR CONFIGS
            print("INVALID INPUT, PLEASE CHOSE THE CORRECT CURRENCY!")
            return request()
        time.sleep(0.3)

        #client.latest(base_currency='EUR')
        send = client.latest(base_currency=input_prim,currencies=[input_prim])['data'][input_prim]
        recive = client.latest(base_currency=input_prim,currencies=[input_scnd])['data'][input_scnd]

        fixed_prim = round((send * input_value), 2)
        fixed_scnd = round((recive * input_value), 2)
        ##apiCalls = req.headers.get('x-ratelimit-remaining-quota-month')

        print(fixed_prim,":", (input_prim)," = ", fixed_scnd,":", (input_scnd))
        #print(f"Calls Left: {apiCalls}")
    else:
        print(f"Error raised, {req.status_code}")
request()

###DONE###