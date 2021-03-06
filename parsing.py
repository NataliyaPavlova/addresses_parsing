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
import requests
import re
import json


class WebPage():

    def __init__(self, url):
        self.url = url
    
    def download(self):
        ''' download text from web-page and save as a list of addresses '''
        r = requests.get(self.url)
        self.addrs_lst = str(r.content).split('\\n')


class Adresses(WebPage):

    def check_punycode(self, string):
        ''' check if domain is punycode and decode it '''
        if re.search('(\A)xn--', string): 
            string = string.encode().decode('idna') 
        return string

    def parse(self):
        ''' iterate through the list of addresses and parse it to dicts'''
        self.lst=[]
        for string in self.addrs_lst:
            if not re.search('(\A)http', string): 
                string = string.strip('b\"').strip('\"')
                if not string:
                    continue
            #if address doesn't start with 'http': default protocol is 'http'
            if len(string.split('://'))==1:
                protocol = 'http'
                part1, rel_url = re.split('/', string.split('://')[0], 1)              
            else:
                protocol = string.split('://')[0]
                part1, rel_url = re.split('/', string.split('://')[1], 1)

            dct = {'protocol' : protocol}
            
            #check if IP (do not validate IP address, only simple check)
            if re.match('^[0-9\.]*$', part1):
                dct['ip'] = part1
            else: 
                domain = self.check_punycode(part1)
                dct['domain'] = domain
            
            dct['rel_url'] = '/' + rel_url
            self.lst.append(dct)
        
      
class Answer(Adresses, WebPage):

    def __init__(self, url, filename):
        WebPage.__init__(self, url)
        self.filename = filename

    def jsonify(self):
        ''' save the list of dicts to the given file'''
        with open(self.filename, 'w') as outfile:
            json.dump(self.lst, outfile)


url = 'https://openphish.com/feed.txt'
filename = 'result.json' #for saving the result

answer = Answer(url, filename)
answer.download()
answer.parse()
answer.jsonify()
