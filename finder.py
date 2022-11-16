import requests

letters_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
arg_error = 'Please enter only latin letters and spacebar'
while True:
    try:
        req = str(input('looking for...'))
    except:
        print(arg_error)
        continue

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
u2 = 'https://musicstax.com/search?q=' + req

s = requests.get(u2)

print(s)