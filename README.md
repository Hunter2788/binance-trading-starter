# 📈 Binance Starter Bot

A simple, modular Python trading bot for Binance Spot markets using an EMA (50) strategy on a 15-minute timeframe.

---

# ⚠️ IMPORTANT DISCLAIMER

This project is for **educational purposes only**.

### You are responsible for:
- Any financial losses
- Any trades executed by this bot
- Proper handling of API keys

This bot:
- does NOT guarantee profit
- has no built-in risk management
- can execute real trades on a live account

Use at your own risk.

---

# 🧠 Strategy Overview

This bot uses a simple EMA (Exponential Moving Average) strategy:

- Indicator: EMA (50)
- Timeframe: 15 minutes

### Trading Rules

| Condition | Action |
|----------|--------|
| Price > EMA | SELL signal |
| Price < EMA | BUY signal |

---

# ⚙️ Features

- Binance Spot API integration
- EMA-based trading logic
- 15-minute automated execution loop
- Modular Python architecture
- Testnet support for safe testing
- Secure API key separation

---

# 📁 Project Structure

```txt
binance-starter-bot/
│
├── bot/
│   ├── main.py          # Bot entry point
│   ├── config.py        # Trading settings
│   ├── strategy.py      # EMA logic
│   ├── trader.py        # Order execution
│   └── logger.py        # Logging system
│
├── keys.py              # API keys (DO NOT UPLOAD)
├── requirements.txt
└── README.md
