#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
# 85.81% 5.02%
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if len(nums) == 0:
#             return 0
#         if len(nums) <= 2:
#             return max(nums)
#         dp = []
#         dp.append([0, 0])
#         dp.append([nums[0], 0])
#         for i in range(1, len(nums)):
#             t1 = max(dp[-2] + dp[-1][1:]) + nums[i] # use self
#             t2 = max(dp[-1])
#             dp.append([t1, t2])
#         return max(dp[-1])

# 66.9% 5.49%     
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        dp = []
        dp.append(nums[0])
        dp.append(max(nums[0], nums[1]))
        for i in range(2, len(nums)):
            dp.append(max(dp[-2] + nums[i], dp[-1]))
        return dp[-1]
# @lc code=end

