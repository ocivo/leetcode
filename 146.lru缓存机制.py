#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#

# @lc code=start
# 82.32% 5.12%
class Node(object):
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.dict = {}
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        else:
            self.update_latest(key)
            return self.dict[key]["val"]

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.update_latest(key)
            self.dict[key]["val"] = value
            self.dict[key]["node"].val = key
        else:
            node = Node(key, None, None)
            if self.capacity == 1:
                if self.size == 1:
                    del self.dict[self.head.val]
                else:
                    self.size = 1
                self.head = node
            elif self.size == 0:
                self.head = node
                self.size += 1
            elif self.size == 1:

                node.next = self.head
                node.prev = None
                self.head.prev = node
                self.head.next = None
                self.tail = self.head
                self.head = node
                self.size += 1
            elif self.size < self.capacity:
                node.next = self.head
                self.head.prev = node
                self.head = node
                self.size += 1
            else:
                tail_key = self.tail.val
                tail_node = self.dict[tail_key]["node"]
                tail_node.prev.next = None
                self.tail = tail_node.prev
                del self.dict[tail_key]

                node.next = self.head
                self.head.prev = node
                self.head = node

            self.dict[key] = {
                "val": value,
                "node": node
            }

    def update_latest(self, key):
        if self.capacity == 1:
            return
        if key == self.head.val:
            return 
        if key == self.tail.val:
            tmp = self.tail
            self.tail.prev.next = None
            self.tail = self.tail.prev
            self.head.prev = tmp
            tmp.next = self.head
            self.head = tmp
            return
        node = self.dict[key]["node"]
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = self.head
        self.head.prev = node
        self.head = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
    
