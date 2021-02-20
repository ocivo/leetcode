#
# @lc app=leetcode.cn id=354 lang=python3
#
# [354] 俄罗斯套娃信封问题
#
from typing import *
import functools
# @lc code=start
# 84.32 % 6.1% Offcial
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if len(envelopes) <= 1:
            return len(envelopes)

        envelopes.sort(key=lambda x: (x[0], -x[1]))

        def lis(nums):
            dp = []
            for i in range(len(nums)):
                idx = bisect_left(dp, nums[i])
                if idx == len(dp):
                    dp.append(nums[i])
                else:
                    dp[idx] = nums[i]
            return len(dp)
        # extract the second dimension and run the LIS
        return lis([i[1] for i in envelopes])

        # dp = [1 for _ in range(len(envelopes))]

        # envelopes.sort(key=functools.cmp_to_key(lambda x, y: x[0] - y[0] if x[0] != y[0] else x[1] - y[1]))

        # for i, env in enumerate(envelopes):
        #     dp[i] = max(dp[i], 1)
        #     for j, cmp_env in enumerate(envelopes[i+1:]):
        #         if cmp_env[0] > env[0] and cmp_env[1] > env[1]:
        #             dp[i + j + 1] = max(dp[i] + 1, dp[i+j+1])
        # return max(dp)



        
        ######################################################
        # envelopes2 = [*envelopes]
        # envelopes.sort(key=functools.cmp_to_key(lambda x, y: y[0] - x[0] if x[0] != y[0] else y[1] - x[1]))
        # envelopes2.sort(key=functools.cmp_to_key(lambda x, y: y[1] - x[1] if x[1] != y[1] else y[0] - x[0]))
        # envs = [envelopes, envelopes2]
        # print(envelopes)
        # print(envelopes2)

        # for i, env in enumerate(envelopes):
        #     dp[str(env)] = [i, None, None] # 索引W, 索引H, 最大值

        # for i, env in enumerate(envelopes2):
        #     dp[str(env)][1] = i

        # final_max = 0

        # def get_closed_max(env, whidx):
        #     for closed_env in envs[whidx][dp[str(env)][whidx] + 1:]:
        #         if env[0] > closed_env[0] and env[1] > closed_env[1]:
        #             if dp[str(closed_env)][2] is None:
        #                 dp[str(closed_env)][2] = max(
        #                     get_closed_max(closed_env, 0),
        #                     get_closed_max(closed_env, 1)
        #                 ) + 1
        #             return dp[str(closed_env)][2]
        #     return 0

        # for i, env in enumerate(envelopes):
        #     if dp[str(env)][2] is None:
        #         dp[str(env)][2] = max(
        #             get_closed_max(env, 0),
        #             get_closed_max(env, 1)
        #         ) + 1
        #         if dp[str(env)][2] > final_max:
        #             final_max = dp[str(env)][2]

        # return final_max

        ######################################################
        # self.final_maxarr = []

        # def backtrace(m, n, maxarr):
        #     if n > len(envelopes) - 1:
        #         if len(maxarr) > len(self.final_maxarr):
        #             self.final_maxarr = [*maxarr]
        #         return
        #     e1 = envelopes[m]
        #     e2 = envelopes[n]
        #     if e2[1] > e1[1] and e2[0] > e1[0]:
        #         maxarr.append(e2)
        #         backtrace(n, n+1, maxarr)
        #         maxarr.pop()
        #     backtrace(m, n+1, maxarr)

        # for i in range(len(envelopes)):
        #     if envelopes[i] in self.final_maxarr:
        #         continue
        #     maxarr = [envelopes[i]]
        #     backtrace(i, i + 1, maxarr)
        # return len(self.final_maxarr)


        
# @lc code=end

