
import pandas as pd
import numpy as np
import requests, jsonv


tx_hash = input()

url_tx_hash = requests.get('http://challenge-server.code-check.io/' + tx_hash)
json_read = json.loads(url_tx_hash.text)

print(json_read['tx_hash'])

