import pandas as pd

def calculate_ema(df, period=50):
    return df["close"].ewm(span=period, adjust=False).mean()

def get_signal(df, ema):
    price = df["close"].iloc[-1]
    ema_val = ema.iloc[-1]

    if price > ema_val:
        return "SELL"
    elif price < ema_val:
        return "BUY"
    return "HOLD"
