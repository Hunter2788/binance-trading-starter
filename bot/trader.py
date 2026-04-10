from binance.client import Client
from keys import API_KEY, API_SECRET
from bot.config import SYMBOL, TRADE_QUANTITY, USE_TESTNET

class Trader:
    def __init__(self):
        self.client = Client(API_KEY, API_SECRET)

        if USE_TESTNET:
            self.client.API_URL = "https://testnet.binance.vision/api"

    def buy(self):
        return self.client.order_market_buy(
            symbol=SYMBOL,
            quantity=TRADE_QUANTITY
        )

    def sell(self):
        return self.client.order_market_sell(
            symbol=SYMBOL,
            quantity=TRADE_QUANTITY
        )
