import ccxt
import random

apiKey = "kpeJqdGoOWyp4xAyPkOEuPrAYlsqYpqA8qAylhtBICO1ca1exOvm4D2o5ksxlQus"
secretkey = "YmvDFSqA6N8PFeZnwWtuqpouoPVypJPPTF6CmNBEgIZrOdzQep9Vlq5ZiweYvKDv"
exchange = ccxt.binance()
exchange.apiKey = apiKey
exchange.secret = secretkey
binance2 = exchange.fetch_balance()
orderbook = exchange.fetch_order_book(symbol="BTC/USDT", limit=5)
print(orderbook)

# if exchange.has['fetchTicker']:
#     print(exchange.fetch_ticker('ETH/BTC'))  # ticker for LTC/ZEC
    # symbols = list(exchange.markets.keys())
    # print(exchange.fetch_ticker(random.choice(symbols)))  # ticker for a random symbol
