import random

with open('my_file.txt', 'w') as f:
    for _ in range(10):
        f.write('a' * random.randint(0, 100))
        f.write('\n')

value = [len(x) for x in open('my_file.txt', 'rb')]
print(value)

it = (len(x) for x in open('my_file.txt', 'rb'))
print(it)


print(next(it))
print(next(it))

roots = ((x, x ** 0.5) for x in it)

print(next(roots))