#! /usr/bin/env
import requests


urls = {
    'url_1': 'http://httpbin.org/ip',
    'url_2': 'https://api.github.com/'
}


def wget_1(url):
    wget = requests.get(url, auth=('user', 'pass'))
    print (wget.status_code)
    print(wget.headers['content-type'])
    print(len(urls))

def wget_2(url):
    wget = requests.get(url)
    return wget.text


# go
def init():
    #wget_1(urls['url_1'])
    print(wget_2(urls['url_2']))


init()

