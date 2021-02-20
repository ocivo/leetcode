#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

# @lc code=start
# 97.02% 57.57%
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return []
        def dfs(a, b):
            nonlocal n, m
            if a < 0 or a > n - 1 or b < 0 or b > m - 1:
                return
            if board[a][b] == "O":
                board[a][b] = "Z"
                dfs(a - 1, b)
                dfs(a + 1, b)
                dfs(a, b - 1)
                dfs(a, b + 1)
        n = len(board)
        m = len(board[0])

        for i in range(n):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][m - 1] == "O":
                dfs(i, m - 1)
        for i in range(m):
            if board[0][i] == "O":
                dfs(0, i)
            if board[n - 1][i] == "O":
                print(i)
                dfs(n-1, i)
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "Z":
                    board[i][j] = "O"
                
# @lc code=end

