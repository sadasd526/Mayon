# https://sales.starpets.gg/api/best/products

import requests
import json
import time, asyncio
from threading import Thread
itemid = 13134
purchasePrice = 2.28

def get_products():
    payload = {"currency": "rub", "id": itemid}
    r = requests.post("https://sales.starpets.gg/api/best/products", json={"currency": "rub", "id": itemid},  cookies={'access-token':"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2NDU2MzU1MywianRpIjoiYmQ3OGVlN2UtZjE4My00ZGE4LWFmZTgtOGE5MjgzNTE5NjRkIiwibmJmIjoxNjY0NTYzNTUzLCJ0eXBlIjoiYWNjZXNzIiwic3ViIjp7ImlkIjoiNjEzNWY0MDE0MTA5NDc1ZGFjMGI1YmEyIiwiZW1haWwiOiJzaGVzdGFrb3ZhLnNpbWFAZ21haWwuY29tIiwidXNlcm5hbWUiOiJTaW1hX1NoZXMiLCJ1c2VybmFtZV9sb3dlcmNhc2UiOiJzaW1hX3NoZXMiLCJiYWxhbmNlIjp7InVzZCI6MC4wLCJydWIiOjEyLjg2OTk5OTk5OTk5OTk0NCwiZXVyIjo3Ljc3MTU2MTE3MjM3NjA5NmUtMTZ9LCJiYWxhbmNlX29mZnNldCI6eyJ1c2QiOjAuMCwicnViIjowLjAsImV1ciI6MC4wfSwicmVmX2NvZGUiOiIiLCJhdmF0YXJfdXJsIjoiMyIsIm1haW5fbGFuZ3VhZ2UiOiJydSIsIm1haW5fY3VycmVuY3kiOiJydWIiLCJtYWluX2NvdW50cnkiOiJSVSJ9LCJleHAiOjE2NjQ2NDk5NTN9.Ns41dfx5uFoZIG-MD73CS-wSrkQ8fMDPFnS_sLeBV_4"})
    return r.json()

# https://sales.starpets.gg/api/buy
def buy_product(id, price):
    payload = {'items' : {'id': itemid, 'price': price}}
    r = requests.post("https://sales.starpets.gg/api/buy", headers = {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2NDU2MzU1MywianRpIjoiYmQ3OGVlN2UtZjE4My00ZGE4LWFmZTgtOGE5MjgzNTE5NjRkIiwibmJmIjoxNjY0NTYzNTUzLCJ0eXBlIjoiYWNjZXNzIiwic3ViIjp7ImlkIjoiNjEzNWY0MDE0MTA5NDc1ZGFjMGI1YmEyIiwiZW1haWwiOiJzaGVzdGFrb3ZhLnNpbWFAZ21haWwuY29tIiwidXNlcm5hbWUiOiJTaW1hX1NoZXMiLCJ1c2VybmFtZV9sb3dlcmNhc2UiOiJzaW1hX3NoZXMiLCJiYWxhbmNlIjp7InVzZCI6MC4wLCJydWIiOjEyLjg2OTk5OTk5OTk5OTk0NCwiZXVyIjo3Ljc3MTU2MTE3MjM3NjA5NmUtMTZ9LCJiYWxhbmNlX29mZnNldCI6eyJ1c2QiOjAuMCwicnViIjowLjAsImV1ciI6MC4wfSwicmVmX2NvZGUiOiIiLCJhdmF0YXJfdXJsIjoiMyIsIm1haW5fbGFuZ3VhZ2UiOiJydSIsIm1haW5fY3VycmVuY3kiOiJydWIiLCJtYWluX2NvdW50cnkiOiJSVSJ9LCJleHAiOjE2NjQ2NDk5NTN9.Ns41dfx5uFoZIG-MD73CS-wSrkQ8fMDPFnS_sLeBV_4",
    "content-type": "application/json",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"104\", \"Opera\";v=\"90\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site"
  },
  data= "{\"items\":[{\"id\":\" "+ str(id) + "\",\"price\":" + str(price) + "}]}",)
    return r.json()

def get_inventory():
    r = requests.get('https://items.starpets.gg/api/items/?userId=6135f4014109475dac0b5ba2', headers = {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2NDU2MzU1MywianRpIjoiYmQ3OGVlN2UtZjE4My00ZGE4LWFmZTgtOGE5MjgzNTE5NjRkIiwibmJmIjoxNjY0NTYzNTUzLCJ0eXBlIjoiYWNjZXNzIiwic3ViIjp7ImlkIjoiNjEzNWY0MDE0MTA5NDc1ZGFjMGI1YmEyIiwiZW1haWwiOiJzaGVzdGFrb3ZhLnNpbWFAZ21haWwuY29tIiwidXNlcm5hbWUiOiJTaW1hX1NoZXMiLCJ1c2VybmFtZV9sb3dlcmNhc2UiOiJzaW1hX3NoZXMiLCJiYWxhbmNlIjp7InVzZCI6MC4wLCJydWIiOjEyLjg2OTk5OTk5OTk5OTk0NCwiZXVyIjo3Ljc3MTU2MTE3MjM3NjA5NmUtMTZ9LCJiYWxhbmNlX29mZnNldCI6eyJ1c2QiOjAuMCwicnViIjowLjAsImV1ciI6MC4wfSwicmVmX2NvZGUiOiIiLCJhdmF0YXJfdXJsIjoiMyIsIm1haW5fbGFuZ3VhZ2UiOiJydSIsIm1haW5fY3VycmVuY3kiOiJydWIiLCJtYWluX2NvdW50cnkiOiJSVSJ9LCJleHAiOjE2NjQ2NDk5NTN9.Ns41dfx5uFoZIG-MD73CS-wSrkQ8fMDPFnS_sLeBV_4",
    "content-type": "application/json",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"104\", \"Opera\";v=\"90\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site"
  })
    
    inv = r.json()

    lis = {}
    lis['items'] = []
    lis['currency'] = 'rub'

    for i in inv['items']:
        lis['items'].append(i['goodId'])
    

    r = requests.post('https://trades.starpets.gg/api/goods/info', headers = {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2NDU2MzU1MywianRpIjoiYmQ3OGVlN2UtZjE4My00ZGE4LWFmZTgtOGE5MjgzNTE5NjRkIiwibmJmIjoxNjY0NTYzNTUzLCJ0eXBlIjoiYWNjZXNzIiwic3ViIjp7ImlkIjoiNjEzNWY0MDE0MTA5NDc1ZGFjMGI1YmEyIiwiZW1haWwiOiJzaGVzdGFrb3ZhLnNpbWFAZ21haWwuY29tIiwidXNlcm5hbWUiOiJTaW1hX1NoZXMiLCJ1c2VybmFtZV9sb3dlcmNhc2UiOiJzaW1hX3NoZXMiLCJiYWxhbmNlIjp7InVzZCI6MC4wLCJydWIiOjEyLjg2OTk5OTk5OTk5OTk0NCwiZXVyIjo3Ljc3MTU2MTE3MjM3NjA5NmUtMTZ9LCJiYWxhbmNlX29mZnNldCI6eyJ1c2QiOjAuMCwicnViIjowLjAsImV1ciI6MC4wfSwicmVmX2NvZGUiOiIiLCJhdmF0YXJfdXJsIjoiMyIsIm1haW5fbGFuZ3VhZ2UiOiJydSIsIm1haW5fY3VycmVuY3kiOiJydWIiLCJtYWluX2NvdW50cnkiOiJSVSJ9LCJleHAiOjE2NjQ2NDk5NTN9.Ns41dfx5uFoZIG-MD73CS-wSrkQ8fMDPFnS_sLeBV_4",
    "content-type": "application/json",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"104\", \"Opera\";v=\"90\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site"
  }, data = json.dumps(lis) )

    inv2 = r.json()

    for v in inv['items']:
        for i in inv2:
            if i['goodId'] == v['goodId']:
                v['id'] = i['id']
                if i['id'] == itemid:
                    global purchasePrice
                    purchasePrice = float(i['purchasePrice'])
    return inv

def trade():
    inv = get_inventory()
    id1 = ""
    trad = []
    uniq = []
    goodId = ""
    for i in inv['items']:
        if i['id'] == itemid:
            uniq.append(i['uniqueId'])
            trad.append(i)
            goodId = i['goodId']

    lis = {"items":{"user":[{"goodId": goodId ,"price":  purchasePrice,"uniqueIds":uniq}],"site":[]},"currency":"rub"}
    print(lis)

    r = requests.post('https://trades.starpets.gg/api/items/trade', headers = {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2NDU2MzU1MywianRpIjoiYmQ3OGVlN2UtZjE4My00ZGE4LWFmZTgtOGE5MjgzNTE5NjRkIiwibmJmIjoxNjY0NTYzNTUzLCJ0eXBlIjoiYWNjZXNzIiwic3ViIjp7ImlkIjoiNjEzNWY0MDE0MTA5NDc1ZGFjMGI1YmEyIiwiZW1haWwiOiJzaGVzdGFrb3ZhLnNpbWFAZ21haWwuY29tIiwidXNlcm5hbWUiOiJTaW1hX1NoZXMiLCJ1c2VybmFtZV9sb3dlcmNhc2UiOiJzaW1hX3NoZXMiLCJiYWxhbmNlIjp7InVzZCI6MC4wLCJydWIiOjEyLjg2OTk5OTk5OTk5OTk0NCwiZXVyIjo3Ljc3MTU2MTE3MjM3NjA5NmUtMTZ9LCJiYWxhbmNlX29mZnNldCI6eyJ1c2QiOjAuMCwicnViIjowLjAsImV1ciI6MC4wfSwicmVmX2NvZGUiOiIiLCJhdmF0YXJfdXJsIjoiMyIsIm1haW5fbGFuZ3VhZ2UiOiJydSIsIm1haW5fY3VycmVuY3kiOiJydWIiLCJtYWluX2NvdW50cnkiOiJSVSJ9LCJleHAiOjE2NjQ2NDk5NTN9.Ns41dfx5uFoZIG-MD73CS-wSrkQ8fMDPFnS_sLeBV_4",
    "content-type": "application/json",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"104\", \"Opera\";v=\"90\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site"
  }, data = json.dumps(lis) )

    print(r.json())



#     inventory = ''
#     # ignore this "{\"items\":{\"user\":[{\"goodId\":\"62ae1a5a277940d7b71389b1\",\"price\":1.7,\"uniqueIds\":[\"633534b747fd6ff683632e4b\"]}],\"site\":[]},\"currency\":\"rub\"}"

#     # get inventory

while True:
    products = get_products()['items']
    for i in products:
        print(i)
        if i['price'] < purchasePrice:
            buy_product(i['id'], i['price'])
        time.sleep(0.1)
    Thread(target=trade).start()
    time.sleep(0.3)

#     fetch("https://trades.starpets.gg/api/items", {
#   "headers": {
#     "accept": "*/*",
#     "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
#     "content-type": "application/json",
#     "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"104\", \"Opera\";v=\"90\"",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "\"Windows\"",
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-site"
#   },
#   "referrer": "https://starpets.gg/",
#   "referrerPolicy": "strict-origin-when-cross-origin",
#   "body": "{\"currency\":\"rub\",\"filter\":{\"types\":[{\"type\":\"egg\"},{\"type\":\"pet\"},{\"type\":\"potion\"},{\"type\":\"transport\"}]},\"sort\":{\"popularity\":\"desc\"}}",
#   "method": "POST",
#   "mode": "cors",
#   "credentials": "omit"
# });
