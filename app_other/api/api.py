#! /usr/bin/env
import requests
import json

urls = [
    'http://httpbin.org/ip',
    'https://api.github.com/',
    'http://api.open-notify.org/iss-pass.json'
]


def wget_1(url):
    res = requests.get(url, auth=('user', 'pass'))
    print (res.status_code)
    print(res.headers['content-type'])
    print(len(urls))

def wget_2(url):
    res = requests.get(url)
    return res.text

def get_1(url):

    coord = {
        "lat": 42,
        "lon": 71
    }

    res_api = requests.get(url, params=coord)
    content = res_api.content

    to_dict = json.loads(content)
    json_f = json.dumps(to_dict, indent=4)
    return json_f


# go
def init():
    #wget_1(urls[0])
    #print(wget_2(urls[1]))
    print(get_1(urls[2]))


init()

