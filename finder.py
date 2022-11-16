import requests

req = str(input('looking for...')).replace(' ','+').lower()

user_headers = {
    'User-Agent': 'PostmanRuntime/7.29.2',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-origin'
}

url_req = 'https://musicstax.com/search?q=' + req

session = requests.session()

response = session.get(url_req).text.splitlines() 

i = 0
while i < len(response):
    if response[i].startswith('<a data-cy="song-image" class="song-image search-image" href="/') is True:
        song_url = str(response[i])
        break
    else:
        i += 1

song_url = song_url[62:]
song_url = song_url[:(len(song_url)-2)]
song_url = 'https://musicstax.com' + song_url

song_response = session.get(song_url).text.splitlines()

j = 0
while j < len(song_response):
    if song_response[j].startswith('<div class="song-meta-title">'):
        info = song_response[j+3]
        break
    else:
        j += 1

key = (info[info.find('data-cy="meta-Key-value">')+25:info.find('data-cy="meta-Key-value">')+25+5])
tempo = (info[info.find('data-cy="meta-Tempo-value">')+27:info.find('data-cy="meta-Tempo-value">')+27+3])
if tempo[2:] == "<":
    tempo = tempo[:2]
else: 
    tempo = tempo

print(f"The Song is probably in \n {key} \n\n Tempo \n {tempo} BPM")