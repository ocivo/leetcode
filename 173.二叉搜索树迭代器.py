#
# @lc app=leetcode.cn id=173 lang=python3
#
# [173] 二叉搜索树迭代器
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 74.84% 5.24%
# class LinkNode:

#     def __init__(self, x, next=None):
#         self.val = x
#         self.next = next

# class BSTIterator:

#     def __init__(self, root: TreeNode):
#         self.head = None
#         self.node = None
#         self.traverse(root)

#     def traverse(self, root):
#         if root is None:
#             return
#         self.traverse(root.left)
#         if self.head is None:
#             self.head = LinkNode(root.val, None)
#             self.node = self.head
#         else:
#             self.node.next = LinkNode(root.val, None)
#             self.node = self.node.next
#         self.traverse(root.right)

#     def next(self) -> int:
#         """
#         @return the next smallest number
#         """
#         x = self.head.val
#         self.head = self.head.next
#         return x


#     def hasNext(self) -> bool:
#         """
#         @return whether we have a next smallest number
#         """
#         return self.head is not None

# 95.34% 9.1%
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.find_min(root)

    def find_min(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        node = self.stack.pop()
        if node.right:
            self.find_min(node.right)
        return node.val


    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) != 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

