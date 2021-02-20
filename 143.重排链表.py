#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#

# @lc code=start
# Definition for singly-linked list.
# 95.59% 56.8%
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return None
        if head.next is None:
            return head
        s = []
        while head.next is not None:
            s.append(head)
            head = head.next
        s.append(head)
        head = s[0]
        rangex = (len(s) + 1) // 2
        for i in range(rangex):
            head.next = s[-(i + 1)]
            head = head.next
            if i + 1 <  rangex:
                head.next = s[i + 1]
                head = head.next
            else:
                head.next = None
