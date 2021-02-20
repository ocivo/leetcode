#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] 整数拆分
#

# @lc code=start
# 33.44% 10.19%
class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 1:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        return self.max_value(n)

    # @lru_cache()
    def max_value(self, n):
        if n <= 3:
            return n
        return max(self.max_value(n-2) * 2, self.max_value(n-3) * 3)
# @lc code=end

