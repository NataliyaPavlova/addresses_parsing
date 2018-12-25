#!/usr/bin/python3

'''
Задание:
Имеется список адресов, выложенный на https://openphish.com/feed.txt
Необходимо написать скрипт-парсер, который
1) скачивает данные
2) парсит данные, выделив в словарь с соответствующими ключами:
               - протокол 
               - домен/IP-адрес
               - относительный URL
3) полученный результат сохраняет в файл в виде списка из словарей
               [{...}, {...}]
Примечание:
- необходимо использовать Python 3
- если протокол явно не указан, использовать в качестве значения 'http'
- если хост указан как IP-адрес, то использовать ключ словаря 'ip', если как доменное имя - ключ 'domain'
- если доменное имя - Punycode (https://ru.wikipedia.org/wiki/Punycode), то необходимо преобразовать его в кодировку utf-8
Пример:
               https://google.com/robots.txt --> {"protocol": "https", "domain": "google.com", "rel_url": "/robots.txt"}
               127.0.0.1 --> {"protocol": "http", "ip": "127.0.0.1", "rel_url": "/"}
               http://xn--90adear.xn--p1ai/ --> {'protocol': 'http', 'domain': 'гибдд.рф', 'rel_url': '/'}
'''
import pprint
import requests
import json

web-page ->  download (make )





def download(url):
    r = requests.get(url)
    lst_addreses = str(r.content).split('\\n')
    return lst_addreses

def rec(data, filename):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)
    

def parsing(lst_addresses):
    for address in lst_addresses:
    #if starts with digits -> parse_ip
    #else: -> parse_domain
    #return lst_dct

url = 'https://openphish.com/feed.txt'
filename = 'result.json'


data = parsing(download(url))
rec(data, filename)
