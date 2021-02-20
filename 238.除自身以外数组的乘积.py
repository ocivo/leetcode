#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#
from typing import *
# @lc code=start
# 6.6% 8.92%
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dp_left = [None] * len(nums)
        dp_right = [None] * len(nums)
        res =  [None] * len(nums)

        for i in range(len(nums) - 1):
            if i == 0:
                dp_left[i] = nums[0]
            else:
                dp_left[i] = dp_left[i - 1] * nums[i]
        for j in range(len(nums) - 1, 0, -1):
            if j == len(nums) - 1:
                dp_right[j] = nums[-1]
            else:
                dp_right[j] = dp_right[j + 1] * nums[j]

        for i in range(len(nums)):
            if i == 0:
                res[0] = dp_right[1]
            elif i == len(nums) - 1:
                res[i] = dp_left[len(nums) - 2]
            else:
                res[i] = dp_left[i - 1] * dp_right[i + 1]

        return res

# print(Solution().productExceptSelf([1, 2, 3, 4]))
# @lc code=end

