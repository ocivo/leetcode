#
# @lc app=leetcode.cn id=334 lang=python3
#
# [334] 递增的三元子序列
#

# @lc code=start
# 95.26% 10.13%
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        minval = nums[0]
        midval = float("inf")
        for num in nums[1:]:
            if num <= minval:
                minval = num
            elif num <= midval:
                midval = num
            else:
                return True
        return False
# @lc code=end

