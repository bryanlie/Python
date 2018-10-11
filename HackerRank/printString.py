'''
Read an integer N.

Without using any string methods, try to print the following: 

12...N
'''

def gen(n):
    if n == 1:
        return '1'
    else:    
        return (gen(n-1) + str(n))

if __name__ == '__main__':
    n = int(input())
    
    print(gen(n))
