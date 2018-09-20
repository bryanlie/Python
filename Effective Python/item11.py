names = ['Cecilia', 'Lisa', 'Maria']
letters = [len(n) for n in names]
print(letters)

longest_name = None
max_length = 0
for name, count in zip(names, letters):
    if count > max_length:
        longest_name = name
        max_length = count
print(longest_name)
