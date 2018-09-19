matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row ]
print(flat)

squared = [[x**2 for x in row] for row in matrix]
print(squared)

my_list = [
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]],
]
print(my_list)
flat = []
for sub_list in my_list:
    for sub_sub_list in sub_list:
        flat.extend(sub_sub_list)
print(flat)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [x for x in a if x > 4 if x % 2 == 0]
c = [x for x in a if x > 4 and x % 2 == 0]
print(b)
print(c)
assert b and c
assert b == c

filtered = [[x for x in row if x % 3 == 0]
            for row in matrix if sum(row) > 10]
print(filtered)