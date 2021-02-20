#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N皇后
#
# runtime: 21.39% - memory - 5%
class Solution:
    '''
    Extend: flip&rotate
    i: row
    j: column
    '''
    def __init__(self):
        self.boards = []
        self.board = []
        self.n = 0

    def solveNQueens(self, n):
        if n == 1:
            return [['Q']]
        elif n == 2 or n == 3:
            return []
        self.n = n
        self.board = [["." for _ in range(n)] for _ in range(n)]
        self.forward()
        return self.boards

    def forward(self):
        i = 0
        start_j = 0
        while i >= 0:
            set_Q = False
            for j in range(start_j, self.n):
                if not self.isBanned(i, j):
                    self.board[i][j] = 'Q'
                    set_Q = True
                    break
            if not set_Q:
                i, start_j = self.backtrack(i)
            elif i == self.n - 1:
                self.append_boards()
                i, start_j = self.backtrack(i)
            else:
                i += 1
                start_j = 0


    def backtrack(self, i):
        if i < 0:
            return i, 0
        row = self.board[i]
        if 'Q' not in row:
            return self.backtrack(i - 1)
        Q_j = row.index('Q')
        self.board[i][Q_j] = '.'
        return i, Q_j + 1

    def append_boards(self):
        b = ["".join(row) for row in self.board]
        self.boards.append(b)

    def isBanned(self, i, j):
        # Vertical Repeat
        for row in range(self.n):
            if self.board[row][j] == "Q":
                return True

        # Diagonal repeat
        if i > j:
            _j = 0
            _i = i - j
        else:
            _i = 0
            _j = j - i
        # Only Direction \/ Ignore --
        anti = True
        # Because Direction, So There Is No i < 0 or j >= n
        while anti or (_j < self.n and _i >= 0):
            if _i == i and _j == j:
                anti = False
            elif self.board[_i][_j] == "Q":
                return True

            if anti:
                _i += 1
                _j += 1
            else:
                _i -= 1
                _j += 1

        return False

# Offcial
# class Solution:
#     def solveNQueens(self, n):
#         def could_place(row, col):
#             return not (cols[col] + hill_diagonals[row - col] + dale_diagonals[row + col])
        
#         def place_queen(row, col):
#             queens.add((row, col))
#             cols[col] = 1
#             hill_diagonals[row - col] = 1
#             dale_diagonals[row + col] = 1
        
#         def remove_queen(row, col):
#             queens.remove((row, col))
#             cols[col] = 0
#             hill_diagonals[row - col] = 0
#             dale_diagonals[row + col] = 0
        
#         def add_solution():
#             solution = []
#             for _, col in sorted(queens):
#                 solution.append('.' * col + 'Q' + '.' * (n - col - 1))
#             output.append(solution)
        
#         def backtrack(row = 0):
#             for col in range(n):
#                 if could_place(row, col):
#                     place_queen(row, col)
#                     if row + 1 == n:
#                         add_solution()
#                     else:
#                         backtrack(row + 1)
#                     remove_queen(row, col)
        
#         cols = [0] * n
#         hill_diagonals = [0] * (2 * n - 1)
#         dale_diagonals = [0] * (2 * n - 1)
#         queens = set()
#         output = []
#         backtrack()
#         return output
