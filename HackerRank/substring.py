'''
search for a substring, count the occurence

'''

def count_substring(string, sub_string):
    count = 0
    b = ''.join(string)
    s = ''.join(sub_string)
    lb = len(string)
    ls = len(sub_string)
    for i in range(lb - ls+1):
        if b[i:i+ls] == s:
            count += 1


    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
