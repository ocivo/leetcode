#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
# 9.87% 14.77%
class Solution:
    def combine(self, n: int, k: int):
        res = []
        all_num = list(range(1, n + 1))

        if n == 0 or k == 0:
            return res

        def backtrack(nums, cur):
            if len(cur) == k:
                res.append(cur[:])
                return
            for i in range(len(nums)):
                cur.append(nums[i])
                # print(nums, i)
                # print(nums[i:], ".")
                # print(cur)
                backtrack(nums[i+1:], cur)
                cur.pop()

        backtrack(all_num, [])
        return res

# print(Solution().combine(4, 2))
# @lc code=end
