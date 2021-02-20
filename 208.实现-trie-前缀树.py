#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
# %22.22 19.51%
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nodes = {}
        self.is_leaf = False


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if len(word) == 0:
            return
        w = word[0]
        if w not in self.nodes:
            self.nodes[w] = Trie()
        if len(word) == 1:
            self.nodes[w].is_leaf = True
        else:
            self.nodes[w].insert(word[1:])

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if len(word) == 0:
            return False
        elif len(word) == 1:
            return word[0] in self.nodes and self.nodes[word[0]].is_leaf
        else:
            if word[0] in self.nodes:
                return self.nodes[word[0]].search(word[1:])
            else:
                return False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if len(prefix) == 0:
            return False
        elif len(prefix) == 1:
            return prefix[0] in self.nodes
        else:
            if prefix[0] in self.nodes:
                return self.nodes[prefix[0]].startsWith(prefix[1:])
            else:
                return False



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

