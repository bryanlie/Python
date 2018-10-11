'''
The National University conducts an examination of n students in x subjects. 
Your task is to compute the average scores of each student.
'''

n, x = map(int, input().split())

a = []
for _ in range(x):
    a.append(list(map(float, input().split())))

for i in zip(*a):
    print('%0.1f' % (sum(i) / len(i)))
