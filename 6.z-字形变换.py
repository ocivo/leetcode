#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#
# runtime: 79.25% - memory - 94.26%
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        gap = (numRows - 1) * 2

        ret = ""
        for i in range(numRows):
            start = 0
            if i == 0 or i == numRows - 1:
                idx = i
                while idx < len(s):
                    ret += s[idx]

                    start += 1
                    idx = i + start * gap
            else:
                idx = i
                ref = 0
                if idx < len(s):
                    ret += s[idx]
                else:
                    continue
                while True:
                    start += 1
                    ref = start * gap

                    idx_l = ref - i
                    if idx_l < len(s):
                        ret += s[idx_l]
                    else:
                        break

                    idx_r = ref + i

                    if idx_r < len(s):
                        ret += s[idx_r]
                    else:
                        break

        return ret
        

