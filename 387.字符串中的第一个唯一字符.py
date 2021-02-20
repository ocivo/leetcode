#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
# 63.16% 42.91%
class Solution:
    def firstUniqChar(self, s: str) -> int:
        record = {}
        seq = 0
        for i, char in enumerate(s):
            if char not in record:
                record[char] = [seq, i]
                seq += 1
            elif record[char] != None:
                record[char] = None
            else:
                pass
        minseq = float("inf")
        minv = -1
        for k, v in record.items():
            if v is not None and v[0] < minseq:
                minseq = v[0]
                minv = v[1]
        return minv

# @lc code=end

