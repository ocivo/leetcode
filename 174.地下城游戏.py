#
# @lc app=leetcode.cn id=174 lang=python3
#
# [174] 地下城游戏
#

# @lc code=start
# 59.25% 39.73%
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])

        get_owe_hp = lambda x: 0 if x >= 0 else -x

        dungeon[-1][-1] = get_owe_hp(dungeon[-1][-1])

        for col in range(n-2, -1, -1):
            dungeon[m-1][col] -= dungeon[m-1][col+1]
            dungeon[m-1][col] = get_owe_hp(dungeon[m-1][col])
        for row in range(m-2, -1, -1):
            dungeon[row][n-1] -= dungeon[row+1][n-1]
            dungeon[row][n-1] = get_owe_hp(dungeon[row][n-1])

        for row in range(m-2, -1, -1):
            for col in range(n-2, -1, -1):
                dungeon[row][col] -= min(dungeon[row][col+1], dungeon[row+1][col])
                dungeon[row][col] = get_owe_hp(dungeon[row][col])
        return dungeon[0][0] + 1 if dungeon[0][0] > 0 else 1

# @lc code=end
