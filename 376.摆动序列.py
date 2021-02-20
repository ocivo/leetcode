#
# @lc app=leetcode.cn id=376 lang=python3
#
# [376] 摆动序列
#
from typing import * 

# @lc code=start
# 18.01% 19.02%
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        dp = [[None, None] for _ in range(len(nums))] # 0:up, 1:down
        dp[0][0] = dp[0][1] = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp[i][0] = max(dp[i-1][1] + 1, dp[i-1][0])
                dp[i][1] = dp[i-1][1]
            elif nums[i] < nums[i-1]:
                dp[i][0] = dp[i-1][0]
                dp[i][1] = max(dp[i-1][0] + 1, dp[i-1][1])
            else:
                dp[i] = [*dp[i-1]]
        return max(dp[len(nums) - 1][1], dp[len(nums) - 1][0])
            
# t = Solution().wiggleMaxLength([0, 0])
# print(t)



        
# @lc code=end

