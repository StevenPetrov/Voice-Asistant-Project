import json
import math
from collections import defaultdict

import requests

from main.tts_stt import text_to_speech, text_to_speech_bg

data = requests.get("https://www.binance.com/bapi/asset/v2/public/asset-service/product/get-products?includeEtf=true").json()['data']


def crypto_price():
    crypto = defaultdict(dict)
    for value in data:
        if value['s'].endswith("USDT"):
            crypto[value['b']] = {"HIGH": value['h'], "LOW": value['l'], "CURRENT": value['c']}

    result =json.dumps(crypto)
    bitcoin = f"Цената на Биткойн е {math.floor(float(crypto['BTC']['CURRENT']))} долара."
    ethereum = f"Цената на Етериум е {math.floor(float(crypto['ETH']['CURRENT']))} долара."

    list = [bitcoin, ethereum]

    for coin in list:
        text_to_speech_bg(coin)