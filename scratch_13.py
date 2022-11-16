import requests
import re
from urllib3 import poolmanager
import ssl
import cfscrape
import cloudscraper

headers = {
    'User-Agent': 'PostmanRuntime/7.29.2',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'same-origin'
}

u = 'https://tunebat.com/'
u2 = 'https://tunebat.com/Search?q=abba%20money'
u3 = 'https://tunebat.com/Info/Me-Quema-Paulina-Rubio/53wQDVcLnSjGFEcXiNUohq'
#url_req = 'https://tunebat.com/Search?q=' + input(f"Тональность какой композиции вы хотите найти?").lower().replace(' ','%20')


scraper = cloudscraper.create_scraper()

print(scraper.get(u3))