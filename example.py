#!/usr/bin/env python
# rename to bitcoin.1r.60s.py and put in ~.config/argos
import re
from gi.repository import Gio
from datetime import datetime

import time
import json
import requests

def coin():
    data = requests.get("https://api.coinmarketcap.com/v1/ticker/bitcoin/")
    price = data.json()[0]["price_usd"]
    coin_price = float(("{0:.2f}").format(float(price))) 
    return coin_price

usd = float(coin())
lastupdate = datetime.now().strftime("%H:%M:%S")

#print(" $" + str(usd) + " (" + str(lastupdate) + ") | iconName=invest-applet")
print("bitcoin $" + str(usd) + " | iconName=invest-applet")
print("---")
#print("Kraken: $" + str(usd) + " | iconName=gedit bash=gedit terminal=false")
print("---")
