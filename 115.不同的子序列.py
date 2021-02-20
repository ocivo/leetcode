#
# @lc app=leetcode.cn id=115 lang=python3
#
# [115] 不同的子序列
#

# @lc code=start

# ----- Time Limit Exceeded
# class Solution:
#     def numDistinct(self, s: str, t: str) -> int:
#         counter = 0
#         def step(s_1, t_1):
#             nonlocal counter
#             if len(t_1) == 0:
#                 counter += 1
#                 return
#             if len(s_1) == 0:
#                 return
#             for i in range(len(s_1)):
#                 if s_1[i] == t_1[0]:
#                     step(s_1[i+1:], t_1[1:])
#         step(s, t)
#         return counter
# 89.29% 36.42%
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def pri(z):
            for k in z:
                print(k)
        i = len(t)
        j = len(s)
        if i == 0:
            return 0
        if j < i:
            return 0
        dp = [[0] * j for _ in range(i)]
        # print(i, j)
        # pri(dp)
        # print(len(dp), len(dp[0]))
        for _i in range(i):
            for _j in range(_i, j):
                if _j == 0:
                    dp[_i][_j] = 1 if t[_i] == s[_j] else 0
                    continue
                if t[_i] == s[_j]:
                    if _i == 0:
                        dp[_i][_j] = dp[_i][_j - 1] + 1
                    else: 
                        dp[_i][_j] = dp[_i - 1][_j - 1] + dp[_i][_j - 1]
                else:
                    dp[_i][_j] = dp[_i][_j - 1]
        # pri(dp)
        return dp[i-1][j-1]

# Solution().numDistinct("babgbag", "bag")
# Solution().numDistinct("abb", "ab")
# Solution().numDistinct("bbbbb", "bb")
        
# @lc code=end

