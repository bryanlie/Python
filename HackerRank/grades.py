'''

Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

'''

if __name__ == '__main__':

    grades = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        grades.append([name, score])

    grades_sorted = sorted(grades, key=lambda x: (x[1], x[0]))

    student = grades_sorted[0]
    lowest = student[1]
    secondlow = 0
    neg = 1
    while True:
        runup = grades_sorted[neg]
        neg += 1
        if runup[1] > lowest:
            secondlow = runup[1]
            break
    findit = [x[0] for x in grades_sorted if x[1] == secondlow]
    for i in findit:
        print(i)
