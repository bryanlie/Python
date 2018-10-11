'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.

The first line contains . The second line contains an array  arr of  integers each separated by a space.

'''


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
   
    arr.sort()
    max = arr.pop()
    while(True):
        runner_up = arr.pop()
        if runner_up < max:
            print(runup)
            break

