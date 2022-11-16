import requests

user_headers = {
    'User-Agent': 'PostmanRuntime/7.29.2',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-origin'
}

u1 = 'https://musicstax.com/'
u2 = 'https://musicstax.com/search?q=money'

s = requests.get(u2)

print(s)