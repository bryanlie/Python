'''
You are the manager of a supermarket. 
You have a list of  items together with their prices that consumers bought on a particular day. 
Your task is to print each item_name and net_price in order of its first occurrence.

'''



from collections import OrderedDict

n = int(input())

d = {}
od = OrderedDict()
for _ in range(n):
    line = input()
    price = line.split().pop()
    name = line[:-len(price)].strip()
    d[name] = int(price)
    if name in od.keys():
        od[name] += 1
    else:
        od[name] = 1

for n, k in od.items():
    print("{}: Quantity bought: {}, Price: {}".format(n, k, d[n]))
    print("Net Price: {}".format(k * d[n]))

