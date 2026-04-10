import time
import pandas as pd
from binance.client import Client

from bot.config import SYMBOL, INTERVAL, EMA_PERIOD
from bot.strategy import calculate_ema, get_signal
from bot.trader import Trader
from bot.logger import get_logger
from keys import API_KEY, API_SECRET

logger = get_logger()

client = Client(API_KEY, API_SECRET)
trader = Trader()

def get_data():
    candles = client.get_klines(
        symbol=SYMBOL,
        interval=INTERVAL,
        limit=100
    )

    df = pd.DataFrame(candles, columns=[
        "time","open","high","low","close","volume",
        "_","_","_","_","_","_"
    ])

    df["close"] = df["close"].astype(float)
    return df

def run():
    logger.info("EMA Bot started...")

    while True:
        try:
            df = get_data()
            ema = calculate_ema(df, EMA_PERIOD)
            signal = get_signal(df, ema)

            price = df["close"].iloc[-1]

            logger.info(f"Price: {price} | Signal: {signal}")

            if signal == "BUY":
                logger.info("BUY ORDER EXECUTED")
                trader.buy()

            elif signal == "SELL":
                logger.info("SELL ORDER EXECUTED")
                trader.sell()

            else:
                logger.info("NO TRADE")

            time.sleep(900)  # 15 minutes

        except Exception as e:
            logger.error(f"Error: {e}")
            time.sleep(10)

if __name__ == "__main__":
    run()
