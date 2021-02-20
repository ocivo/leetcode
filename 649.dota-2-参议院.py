#
# @lc app=leetcode.cn id=649 lang=python3
#
# [649] Dota2 参议院
#

# @lc code=start
# rewrite official
# 2927 5068
from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        survives = deque()
        rest = [0, 0] # R D
        voting = [0, 0] # R D
        for x in senate:
            nx = (x == 'R') ^ 1
            survives.append(nx)
            rest[nx] += 1
        # print(rest, survives)
        while rest[0] * rest[1] != 0:
            p = survives.popleft()
            # print(voting, p, voting[p ^ 1])
            if voting[1 - p] > 0:
                voting[1 - p] -=1
                rest[p] -= 1
            else:
                voting[p] += 1
                survives.append(p)
            # print(survives, rest)
        # print(survives, rest)
        return 'Radiant' if rest[0] > 0 else 'Dire'

# A = Solution().predictPartyVictory('RDRDD')
# print(A)

# @lc code=end

