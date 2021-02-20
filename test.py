# class Solution:
#     def grayCode(self, n: int):
#         res, head = [0], 1
#         for i in range(n):
#             for j in range(len(res) - 1, -1, -1):
#                 res.append(head + res[j])
#             head <<= 1
#         return res

# for i in range(8):
#     print(Solution().grayCode(i))

# a = TreeNode(0)
# print(int("inf"))

a = ["a a a a a a a", "a a a a a aa", "a a a a aa a", "a a a aa a a", "a aa a a aa", "a a a aaaa", "a a aa a a a", "aa a a a aa", "a a aa aa a", "a a aaaa a", "a aa a a a a", "aa a a a aa", "a a aa aa a", "aa a aa a a", "aa aa a aa",
     "a aa aaaa", "a aaaa a a", "aaaa a aa", "aa a a a a a", "aa a a a aa", "a a aa aa a", "aa a aa a a", "aa aa a aa", "a aa aaaa", "aa aa a a a", "aa aa a aa", "aa aa aa a", "aa aaaa a", "aaaa a a a", "aaaa a aa", "aaaa aa a"]
b = ["a a a a a a a", "aa a a a a a", "a aa a a a a", "a a aa a a a", "aa aa a a a", "aaaa a a a", "a a a aa a a", "aa a aa a a", "a aa aa a a", "a aaaa a a", "a a a a aa a", "aa a a aa a", "a aa a aa a", "a a aa aa a", "aa aa aa a",
     "aaaa aa a", "a a aaaa a", "aa aaaa a", "a a a a a aa", "aa a a a aa", "a aa a a aa", "a a aa a aa", "aa aa a aa", "aaaa a aa", "a a a aa aa", "aa a aa aa", "a aa aa aa", "a aaaa aa", "a a a aaaa", "aa a aaaa", "a aa aaaa"]
print(len(a))
print(len(b))

count = 0 
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] == a[j]:
            print(a[i], "-------", i, j)

for it in a:
    if it not in b:
        print("False", it)

for it in b:
    if it not in a:
        print("false", it)