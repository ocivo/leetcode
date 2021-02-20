#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#

# @lc code=start
# 88.3% 34.24%
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 0:
            return 0
        if len(triangle) == 1:
            return triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(i + 1):
                s1 = triangle[i-1][j] + triangle[i][j] if j < i else float("inf")
                s2 = triangle[i-1][j-1] + triangle[i][j] if j > 0 else float("inf")
                triangle[i][j] = min(s1, s2)
        return min(triangle[-1])

# Solution.minimumTotal()
# @lc code=end

