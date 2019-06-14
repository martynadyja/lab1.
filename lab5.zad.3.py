#3 Prepare a simulation of transactions between these users.
# Take random user and pair him/her with another one. Assume a random amount but take real world price. Sum up the transaction printing:
# username1 exchanged X.XXX BTC with username2 for PLN YYYYY.YYY PLN. (2p)
# Simulate real time - do not proceed all transactions at once. Try to make around 100 transactions per minute (2p)
# Simulate user's assets. Creating a user assign random amount of a given currency. Take it into account while performing a transaction.
# Remember to amend user's assets after the transaction. (2p)

import requests
from random import random, randint
from time import sleep
import uuid

def bitbay():
    BitBay = requests.get("https://bitbay.net/API/Public/BTCPLN/ticker.json")
    bitbaydata = BitBay.json()
    best_bid_bitbay = bitbaydata['bid']
    best_ask_bitbay = bitbaydata['ask']
    print('bid:', best_bid_bitbay, 'ask:', best_ask_bitbay)
    return best_bid_bitbay, best_ask_bitbay

def tiingo():
    Tiingo = requests.get("https://api.tiingo.com/tiingo/crypto/top?tickers=btcusd&token=5ae14e499938caf8d9f51ad398e80df834a5cd6a")
    tingodata = Tiingo.json()
    best_bid_tingo = (tingodata[0]['topOfBookData'][0]['bidPrice'])
    best_ask_tingo = (tingodata[0]['topOfBookData'][0]['askPrice'])
    print('bid:', best_bid_tingo, 'ask:', best_ask_tingo)
    return best_bid_tingo, best_ask_tingo

class userwallet:
    btc = []
    usd = []

    def __init__(self, btc = None, usd = None):
        if btc is None:
            btc = random()
        if usd is None:
            usd = random() * 1000
        self.btc = btc
        self.usd = usd

    def add_to_wallet(self, currency, amount):
        if currency.lower() == 'usd':
            self.usd += amount
        if currency.lower() == 'btc':
            self.btc += amount

    def remove_from_wallet(self, currency, amount):
        if currency.lower() == 'usd':
            self.usd -= amount
        if currency.lower() == 'btc':
            self.btc -= amount

    def get_wallet(self):
        return self.btc, self.usd

class randomuser:
    id = []
    username = []
    wallet = []

    def __init__(self, id, btc = None, usd = None):
        self.username = self.get_firstname_and_lastname()
        self.wallet = userwallet(btc, usd)
        self.id = uuid.uuid1()

    def get_firstname_and_lastname(self):
        users = requests.get("https://randomuser.me/api/")
        datausers = users.json()
        firstName = datausers['results'][0]['name']['first']
        lastName = datausers['results'][0]['name']['last']
        return firstName, lastName

    def get_username(self):
        return self.username

    def get_user_wallet(self):
        return self.wallet.get_wallet()

    def add_to_user_wallet(self, currency, amount):
        self.wallet.add_to_wallet(currency, amount)

    def remove_from_user_wallet(self, currency, amount):
        self.wallet.remove_from_wallet(currency, amount)

class transaction:
    users = []
    BitBayMarket = []

    def __init__(self, loops = 100):
        for i in range(loops):
            self.users.append(randomuser(i))
        self.BitBayMarket = bitbay()

    def list_of_users(self):
        for user in self.users:
            print("username:", user.get_username()[0].capitalize()+' '+user.get_username()[1].capitalize(), "wallet:", user.get_user_wallet()[0], "BTC,", user.get_user_wallet()[1], "USD.")

    def make_transaction(self):
        first_user = randint(0, len(self.users) - 1)
        second_user = randint(0, len(self.users) - 1)
        while first_user is second_user:
            second_user = randint(0, len(self.users) - 1)
        sell_amount = random()/10

        if sell_amount <= self.users[first_user].get_user_wallet()[0] and sell_amount * self.BitBayMarket[1] <= self.users[second_user].get_user_wallet()[1]:
            self.users[first_user].remove_from_user_wallet('btc', sell_amount)
            self.users[first_user].add_to_user_wallet('usd', sell_amount * self.BitBayMarket[0])
            self.users[second_user].remove_from_user_wallet('usd', sell_amount * self.BitBayMarket[1])
            self.users[second_user].add_to_user_wallet('btc', sell_amount)
            print(self.users[first_user].get_username()[0].capitalize(), self.users[first_user].get_username()[1].capitalize(), "exchanged", sell_amount, "BTC with", self.users[second_user].get_username()[0].capitalize(), self.users[second_user].get_username()[1].capitalize(), "for", sell_amount * self.BitBayMarket[1], "USD.")
            return True
        else:
            print("Transaction canceled.")
            return False

    def multiple_transactions(self, number_of_transactions = None, time = None):
        if number_of_transactions is None:
            number_of_transactions = 100
        if time is None:
            time = 5
        confirmed_transaction = 0
        unconfirmed_transaction = 0

        while confirmed_transaction + unconfirmed_transaction <= 1000:
            if self.make_transaction():
                confirmed_transaction += 1
            else:
                unconfirmed_transaction += 1
            print("confirmed:", confirmed_transaction, "unconfirmed:", unconfirmed_transaction)
            sleep(time)

x = transaction(20)

x.list_of_users()
x.multiple_transactions(100, 0)
x.list_of_users()
