import time
import requests
from pprint import pprint


class WazirX:
    def __init__(self,
                 url='https://api.wazirx.com',
                 key='xxxx',
                 secret='xxxx'):
        self.name = 'wazirx'
        self.url = url
        self.key = key
        self.secret = secret

    def do_get(self, url):
        response = requests.get(url)
        data = response.json()
        # pprint(data)
        return data

    def get_market_status(self):
        url = self.url + '/api/v2/market-status'
        return self.do_get(url)

    def get_market_ticker(self):
        url = self.url + '/api/v2/tickers'
        return self.do_get(url)

    def get_orderbook(self, market):
        url = self.url + '/api/v2/depth?market=' + market
        return self.do_get(url)

    def get_market_trade_history(self, market):
        url = self.url + '/api/v2/trades?market=' + market
        return self.do_get(url)
