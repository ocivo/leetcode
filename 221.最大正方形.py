#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#

# @lc code=start

# 61.52% 14.29%
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row = len(matrix)
        if row == 0:
            return 0
        col = len(matrix[0])
        memory_matrix = [[0 for _ in range(col)] for _ in range(row)]
        max_val = 0

        def get_max_val(i, j):
            if i == 0 or j == 0:
                return 1
            min_val = min(memory_matrix[i-1][j-1], memory_matrix[i][j-1], memory_matrix[i-1][j])
            return min_val + 1

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == '0':
                    continue
                memory_matrix[i][j] = get_max_val(i, j)
                max_val = max(memory_matrix[i][j], max_val)
        
        return max_val * max_val


# @lc code=end
