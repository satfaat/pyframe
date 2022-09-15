import requests

def load_json(url):
    response = requests.get(url)
    return response.json() 


def load_json2(url):
    with requests.Session() as s:
        response = s.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status() 

import urllib.request
import json

def load_json3(url):
    with urllib.request.urlopen(url) as response:
        if(response.getcode() == 200):
            data = response.read()
            jsonData = json.loads(data)
        else:
            print("Error receiving data", response.getcode())

    return jsonData 


import json
from urllib3 import PoolManager

def load_json4(url):
    manager = PoolManager(10)
    response = manager.request('GET', url)
    payload = response.data.decode()

    return json.loads(payload) 