#
# @lc app=leetcode.cn id=140 lang=python3
#
# [140] 单词拆分 II
#
from typing import *

# @lc code=start
# 17:14 - 18:32
# 16.88% 13.39%
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        store = {}

        def backtrace(start_idx):
            if start_idx in store:
                return store[start_idx]
            
            res = []
            if start_idx == len(s):
                res.append("")
            for i in range(start_idx + 1, len(s) + 1):
                if s[start_idx: i] in wordDict:
                    back_res = backtrace(i)
                    for item in back_res:
                        res.append(s[start_idx: i] + (" " if item != "" else "") + item)
            store[start_idx] = res
            return res
        return backtrace(0)

# @lc code=end

