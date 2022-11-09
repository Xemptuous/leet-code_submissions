from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        key = max(strs, key=len)
        trie = Trie()
        for s in strs:
            trie.insert(s)
        
        return trie.longestPrefix(key)


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.isEnd = True

    def longestPrefix(self, word: str):
        node = self.root
        prefix = ""
        for c in word:
            if c in node.children and len(node.children) == 1 and not node.isEnd:
                prefix += c
                node = node.children[c]
            else:
                return prefix
        return prefix

