#
# @lc app=leetcode.cn id=289 lang=python3
#
# [289] 生命游戏
#

# @lc code=start
# %89.16 30.59%
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ms = len(board)
        if ms == 0: return
        ns = len(board[0])
        signals = [[0 for _ in range(ns)] for _ in range(ms)]

        def set_signals(m, n):
            cur = board[m][n]
            s = max(n-1, 0)
            e = min(ns, n+2)
            total = 0
            if m != 0:
                total += sum(board[m-1][s:e])

            total += sum(board[m][s:e])
            
            if m != ms - 1:
                total += sum(board[m+1][s:e])

            if cur == 1:
                if total == 3 or total == 4:
                    signals[m][n] = 1
            else:
                if total == 3:
                    signals[m][n] = 1

        for m in range(ms):
            for n in range(ns):
                set_signals(m, n)
        for m in range(ms):
            for n in range(ns):
                board[m][n] = signals[m][n]
            
# @lc code=end

