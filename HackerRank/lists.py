'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the  types listed above. 
Iterate through each command in order and perform the corresponding operation on your list.

No switch case in Python...
'''



if __name__ == '__main__':
    n = int(input())
    arr = []

    for _ in range(n):
        line = list(input().split())

        if line[0] == 'insert':
            arr.insert(int(line[1]), int(line[2]))
        elif line[0] == 'print':
            print(arr)
        elif line[0] == 'remove':
            arr.remove(int(line[1]))
        elif line[0] == 'append':
            arr.append(int(line[1]))
        elif line[0] == 'sort':
            arr.sort()
        elif line[0] == 'pop':
            arr.pop()
        elif line[0] == 'reverse':
            arr.reverse()
        else:
            break
