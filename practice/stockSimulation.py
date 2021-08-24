import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv("UPST.csv")

returns = np.log(1 + df['Adj Close'].pct_change())

mu, sigma = returns.mean(), returns.std()

# print(mu, sigma)
# mu = 0.01
# sigma = 0.1

sim_rets = np.random.normal(mu, sigma, 5)

start_price = df['Adj Close'].iloc[-1]

prices = start_price * (1 + sim_rets).cumprod()

print(prices)

diff = np.diff(prices)
print(diff)

pos = 0
gain = []
balance = 0.0

for i, d in enumerate(diff):
    if d > 0 and pos == 0:  # buy
        pos = 1
        balance -= prices[i]
    elif d < 0 and pos == 1:    # sell
        pos = 0
        balance += prices[i]
        gain.append(balance)
        balance = 0.0
    elif d >= 0 and pos == 1:  # hold
        pass

if pos == 1:
    pos = 0
    balance += prices[-1]
    gain.append(balance)
    balance = 0.0

print(gain)

print(sorted(gain)[-1])

print(prices.max(), prices.min(), prices.max() - prices.min())

# 2 transactions
def maxProfit(price, n):
    profit = [0] * n

    max_price = price[n-1]
    for i in range(n-2, 0, -1):
        if price[i] > max_price:
            max_price = price[i]
        profit[i] = max(profit[i+1], max_price - price[i])

    print(profit)

    min_price = price[0]

    for i in range(1, n):
        if price[i] < min_price:
            min_price = price[i]
        profit[i] = max(profit[i-1], profit[i] + (price[i] - min_price))

    print(profit)
    return profit[n-1]

# price = [2, 30, 15, 10, 8, 25, 80]
# print(maxProfit(price, len(price)))


