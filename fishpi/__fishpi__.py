import json
import requests

DOMAIN = 'https://fishpi.cn'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Referer': DOMAIN,
}


class Base(object):
    def __init__(self, apiKey=''):
        self.setToken(apiKey)

    def setToken(self, apiKey):
        self.apiKey = apiKey

    def json(self, url, data=None):
        if data is None:
            return requests.get(url=DOMAIN + url, headers=HEADERS).json()

        headers = {
            **HEADERS,
            'Content-Type': 'application/json'
        }

        return requests.post(url=DOMAIN + url, headers=headers, data=json.dumps(data)).json()

    def get(self, url):
        return requests.get(url=DOMAIN + url, headers=HEADERS).text

    def post(self, url, data=None, files=None):
        return requests.post(url=DOMAIN + url, data=data, files=files).json()

    @staticmethod
    def toMetal(sysMetal:str):
        try:
            metal = json.loads(sysMetal)
            for i, m in metal['list']:
                attr = m['attr'].split('&')
                m['attr'] = dict()
                for a in attr:
                    key_val = a.split('=')
                    m['attr'][key_val[0]] = key_val[1]
                
                metal['list'][i] = m
            return metal
        except:
            return {
                list: []
            }        
        
    