#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# 16:49 - 17:01
# 66.13% 5.02%
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        visited = {}
        def copy(node):
            nonlocal visited
            if node is None:
                return None
            if node in visited:
                return visited[node]
            else:
                new_node = Node(node.val, None, None)    
                visited[node] = new_node
                new_node.next = copy(node.next)
                new_node.random = copy(node.random)
                return new_node
        return copy(head)
        
# @lc code=end

