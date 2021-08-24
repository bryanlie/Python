"""
Given a MxN matrix where each element can either be 0 or 1. We need to find the shortest path between a given source
cell to a destination cell. The path can only be created out of a cell if its value is 1.

The idea is inspired from Lee algorithm and uses BFS.

1. We start from the source cell and calls BFS procedure.
2. We maintain a queue to store the coordinates of the matrix and initialize it with the source cell.
3. We also maintain a Boolean array visited of same size as our input matrix and initialize all its elements to false.
    a. We LOOP till queue is not empty
    b. Dequeue front cell from the queue
    c. Return if the destination coordinates have reached.
    d. For each of its four adjacent cells, if the value is 1 and they are not visited yet,
    we enqueue it in the queue and also mark them as visited.
"""

from collections import deque
ROW = 10 #9
COL = 20 #10

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class queueNode:
    def __init__(self, pt, dist):
        self.pt = pt
        self.dist = dist

def isValid(row, col):
    return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)

rowNum = [-1, 0, 0, 1]
colNum = [0, -1, 1, 0]

def BFS(mat, src, dest):
    if mat[src.x][src.y] !=1 or mat[dest.x][dest.y] !=1:
        return -1

    visited = [[False for j in range(COL)] for i in range(ROW)]

    visited[src.x][src.y] = True

    q = deque()
    s = queueNode(src, 0)
    q.append(s)

    while q:
        curr = q.popleft()

        pt = curr.pt
        if pt.x == dest.x and pt.y == dest.y:
            return curr.dist

        for i in range(4):
            row = pt.x + rowNum[i]
            col = pt.y + colNum[i]

            if isValid(row, col) and mat[row][col] ==1 and not visited[row][col]:
                visited[row][col] = True
                Adjcell = queueNode(Point(row, col), curr.dist+1)
                q.append(Adjcell)
    return -1


def main():
    mat = [[1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
           [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
           [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
           [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
           [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
           [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
           [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
           [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
           [1, 1, 0, 0, 0, 0, 1, 0, 0, 1]]
    source = Point(0, 0)
    dest = Point(3, 4)

    a = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
    start = Point(1, 0)
    end = Point(4, 19)

    dist = BFS(a, start, end)

    if dist != -1:
        print("Shortest Path is", dist)
    else:
        print("Shortest Path doesn't exist")

if __name__ == "__main__":
    main()
