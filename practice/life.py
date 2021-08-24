"""
Leetcode 289 Game of Life
Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]
"""
import numpy as np

neighbors = [(0,-1), (0,1), (-1,0), (1,0), (-1,-1), (-1,1), (1,1), (1,-1)]


class Life():
    def __init__(self, board):
        self.m, self.n = np.array(board).shape
        self.board = board

    def update(self):
        for i in range(self.m):
            for j in range(self.n):

                live_neighbors = 0
                for n in neighbors:
                    r = i + n[0]
                    c = j + n[1]
                    # Check the validity of the neighboring cell and if it was originally a live cell.
                    if (r >= 0 and r < self.m) and (c >= 0 and c < self.n) and (abs(self.board[r][c]) == 1):
                        live_neighbors +=1

                if self.board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    self.board[i][j] = -1  # -1 signifies the cell is now dead but originally was live.

                if self.board[i][j] == 0 and live_neighbors == 3:
                    self.board[i][j] = 2  # 2 signifies the cell is now live but was originally dead.

        for i in range(self.m):
            for j in range(self.n):
                if self.board[i][j] > 0:
                    self.board[i][j] = 1
                elif self.board[i][j] <= 0:
                    self.board[i][j] = 0

    def get_mn(self):
        print(self.m, self.n)

    def print_board(self):
        print(self.board)



input = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]

# input = [[1,1],[1,0]]
l = Life(input)
l.get_mn()
l.print_board()
l.update()
l.print_board()

