#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
# runtime: 36.43 % - memory - 97.31 %
class Solution:
	def lengthOfLongestSubstring(self, s):
		store = max_store = ""

		for char in s:
			if char not in store:
				store += char
			else:
				if len(max_store) < len(store):
					max_store = store
				store = store[store.index(char) + 1:] + char

		return max(len(max_store), len(store))

# runtime: 71.69 % - memory - 21.41 %
# class Solution:
# 	def lengthOfLongestSubstring(self, s):
# 		store, max_store = [], []

# 		for char in s:
# 			if char not in store:
# 				store.append(char)
# 			else:
# 				if len(max_store) < len(store):
# 					max_store = store.copy()
# 				store.append(char)
# 				store = store[store.index(char) + 1:]

# 		return max(len(max_store), len(store))
