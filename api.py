import requests

url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
response = requests.get(url)

def getPrice():
    price = 0
    if response.status_code==200:
        json = response.json()
        price = json.get('bpi').get('USD').get('rate')
    return price

def getDate():
    date = 0
    if response.status_code==200:
        json = response.json()
        date = json.get('time').get('updated')
    return date
        
def getCoin():
    coin = 0
    if response.status_code==200:
        json = response.json()
        coin = json.get('bpi').get('USD').get('code')
    return coin
