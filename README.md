# addresses_parsing

# How to start
You should download parsing.py to your computer and launch it in console. It uses Python3.


# What it does
It parses a list of web-addresses from https://openphish.com/feed.txt, make a dict from each address (with keys 'protocol, 'domain'/'ip' and 'rel_url') and saves a list of dicts to the file result.json


'''
Задание:
Имеется список адресов, выложенный на https://openphish.com/feed.txt
Необходимо написать скрипт-парсер, который
1) скачивает данные
2) парсит данные, выделив в словарь с соответствующими ключами:
               - протокол 
               - домен/IP-адрес
               - относительный URL
3) полученный результат сохраняет в файл result.json в виде списка из словарей
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


