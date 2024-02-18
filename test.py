#!/usr/bin/env python
# coding: utf-8

import requests
import os
from dotenv import load_dotenv
load_dotenv()


rest_base_url = "https://api.bitvavo.com/v2/"

json_pair_data = 'https://api.bitvavo.com/v2/ticker/24h'

api_key_name = "abc"
api_secret = "123"

api_key = os.getenv("BITVAVO_API_KEY")

print(api_key)



# curl --location 'https://api.bitvavo.com/v2/order' \
#   --header 'Bitvavo-Access-Key: <replace with your access key>' \
#   --header 'Bitvavo-Access-Signature: <A SHA256 HMAC hex digest of timestamp + method + url + body>' \
#   --header 'Bitvavo-Access-Timestamp: <Current timestamp in milliseconds>' \
#   --header 'Bitvavo-Access-Window: 10000' \
#   --header 'Content-Type: application/json' \
#   --data '{
#     "market": "BTC-EUR",
#     "side": "buy",
#     "orderType": "market",
#     "amount": "10",
#     "responseRequired": true
#   }'
