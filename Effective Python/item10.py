from random import randint

random_bits = 0
for i in range(64):
    if randint(0, 1):
        random_bits |= 1 << i
print(bin(random_bits))

flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']
for flavor in flavor_list:
    print('%s is delicious' % flavor)

for i, flavor in enumerate(flavor_list, 1):
    print('%d: %s' % (i, flavor))