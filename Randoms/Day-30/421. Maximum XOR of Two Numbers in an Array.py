class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = -1           # used to store the value of entire number at the end of trie node

class Trie:
    def __init__(self):
        self.root = TrieNode()  # object of trienode class
    
    def addNum(self, num):
        cur = self.root         # every time start from root
        for i in range(31, -1, -1):
            bit = 1 if num & (1 << i) else 0  # bit value i'th position of num 
            if bit not in cur.children:
                cur.children[bit] = TrieNode()
            cur = cur.children[bit]
        cur.val = num           # storing the value of entire num at the end of trie node
                

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()           # creating object of Trie class
        for num in nums:        # adding all num to the trie structure
            trie.addNum(num)
        
        res = 0
        for num in nums:        
            cur = trie.root     # every time start cur pointer from root
            for i in range(31, -1, -1):
                bit = 1 if num & (1 << i) else 0  # bit value of i'th position of num  
                if bit == 1:                      # try to move towards opposite key ie. 0
                    if 0 in cur.children:         # opposit key 0 exist then defenetly go towards the child 0
                        cur = cur.children[0]
                    else:                         # opposit key 0 not exist so we have only option to go towards what we have ie. 1
                        cur = cur.children[1]
                else:     # bit == 0              # try to move towards opposite key ie. 1
                    if 1 in cur.children:         # opposit key 1 exist then defenetly go towards the child 1
                        cur = cur.children[1]
                    else:                         # opposit key 1 not exist so we have only option to go towards what we have ie. 0
                        cur = cur.children[0]
            # as we tried to maximize the inequality between cur.val and num so XOR of them will give max value
            res = max(res, cur.val ^ num)
        
        return res
