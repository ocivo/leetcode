#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#
from typing import *
# @lc code=start
# 79.78% 6.41%
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        r = None
        count = 0
        for num in nums:
            if count == 0:
                r = num
                count = 1
            elif num != r:
                count -= 1
            else:
                count += 1
        return r


# @lc code=end
