'''

You are given a complex . Your task is to convert it to polar coordinates.

'''

# 
# from cmath import phase
# 
# z = input().split('+')
# 
# real = float(z[0])
# imag = float(z[1][:-1])
# 
# print(math.sqrt(real**2 + imag **2))
# print(phase(complex(real, imag)))


from cmath import polar
print('{}\n{}'.format(*polar(complex(input()))))
