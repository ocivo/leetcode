#
# @lc app=leetcode.cn id=329 lang=python3
#
# [329] 矩阵中的最长递增路径
#

# @lc code=start
# 68.76% 50.21%
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        def gt(i, j, i2, j2):
            if i2 < 0 or i2 > m - 1:
                return False
            elif j2 < 0 or j2 > n -1:
                return False
            else:
                return matrix[i][j] < matrix[i2][j2]
        self.res_max = 0
        def find_max(i, j):
            if i < 0 or i > m - 1:
                return 0
            elif j < 0 or j > n -1:
                return 0
            elif dp[i][j] != 0:
                return dp[i][j]
            else:
                cur_max_value = 0
                if gt(i, j, i-1, j):
                    cur_max_value = max(find_max(i-1, j), cur_max_value)
                if gt(i, j, i+1, j):
                    cur_max_value = max(find_max(i+1, j), cur_max_value)
                if gt(i, j, i, j-1):
                    cur_max_value = max(find_max(i, j-1), cur_max_value)
                if gt(i, j, i, j+1):
                    cur_max_value = max(find_max(i, j+1), cur_max_value)
                cur_max_value += 1
                dp[i][j] = cur_max_value
                if cur_max_value > self.res_max:
                    self.res_max = cur_max_value
                return cur_max_value

        
        for i in range(m):
            for j in range(n):
                dp[i][j] = find_max(i, j)

        return self.res_max
        
# @lc code=end

