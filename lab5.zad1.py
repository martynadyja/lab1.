# 1 Find another public API with cryptocurrency and compare prices. As an output print:
# "Currently the XXX exchange market is better for buying whilst YYY is better for selling" (3p)

import requests

def bitbay():
    BitBay = requests.get("https://bitbay.net/API/Public/BTCPLN/ticker.json")
    bitbaydata = BitBay.json()
    best_bid_bitbay = bitbaydata['bid']
    best_ask_bitbay = bitbaydata['ask']
    print('BitBay bid:', best_bid_bitbay, 'BitBay ask:', best_ask_bitbay)
    return best_bid_bitbay, best_ask_bitbay

def tiingo():
    Tiingo = requests.get("https://api.tiingo.com/tiingo/crypto/top?tickers=btcusd&token=5ae14e499938caf8d9f51ad398e80df834a5cd6a")
    tingodata = Tiingo.json()
    best_bid_tingo = (tingodata[0]['topOfBookData'][0]['bidPrice'])
    best_ask_tingo = (tingodata[0]['topOfBookData'][0]['askPrice'])
    print('Tiingo bid:', best_bid_tingo, 'Tiingo ask:', best_ask_tingo)
    return best_bid_tingo, best_ask_tingo

bitbay = bitbay()
tiingo = tiingo()

if tiingo[0] > bitbay[0] and tiingo[1] > bitbay[1]:
    print("Currently the BitBay exchange market is better for buying whilst Tiingo is better for selling.")
elif tiingo[0] < bitbay[0] and tiingo[1] > bitbay[1]:
    print("Currently the BitBay exchange market is better for buying and BitBay is better for selling.")
elif tiingo[0] > bitbay[0] and tiingo[1] < bitbay[1]:
    print("Currently the Tiingo exchange market is better for buying and Tiingo is better for selling.")
elif tiingo[0] < bitbay[0] and tiingo[1] < bitbay[1]:
    print("Currently the Tiingo exchange market is better for buying whilst BitBay is better for selling.")

