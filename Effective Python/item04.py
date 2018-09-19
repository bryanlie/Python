from urllib.parse import parse_qs

my_values = parse_qs('red=5&blue=0&green=', keep_blank_values = True)
print(repr(my_values))

def get_first_int(values, key, default=0):
    found = values.get(key, [''])
    print(found)
    if found[0]:
        print(found[0])
        found = int(found[0])
    else:
        found = default
    return found

red = get_first_int(my_values, 'red')
green = get_first_int(my_values, 'green')
purple = get_first_int(my_values, 'purple')

print('Red: %r' % red)
print('Green: %r' % green)
print('Purple: %r' % purple)