#
# @lc app=leetcode.cn id=378 lang=python3
#
# [378] 有序矩阵中第K小的元素
#

# @lc code=start
# 5.08% 5.14%
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        colidxs = [0] * m
        while k:
            minv = [float('inf'), None]
            for row, col in enumerate(colidxs):
                if col == n:
                    continue
                if matrix[row][col] < minv[0]:
                    minv = [matrix[row][col], row]
                elif col == 0:
                    break
            colidxs[minv[1]] += 1
            k -= 1
        return minv[0]
# @lc code=end

