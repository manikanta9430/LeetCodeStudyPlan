import queue
class Trie:
    def __init__(self, word=None):
        self.nodes = {}
        if word:
            self.add(word)
    
    def add(self, word, index):
        nodes = self.nodes
        for i, ch in enumerate(word):
            if ch not in nodes:
                nodes[ch] = {}
            nodes = nodes[ch]
        nodes["#"] = index
        
        
    def printTrie(self):
        print(self.nodes)
        
        
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        t = Trie()
        for i, word in enumerate(words):
            if len(word) > 0:
                t.add(word[::-1], i)
            
        
        def isPalindrome(word, start=None, end=None):
            if start is None:
                start = 0
            if end is None:
                end = len(word)-1
            while start < end:
                if word[start] != word[end]:
                    return False
                start += 1
                end -= 1
            return True
        
        def updatePalindromes(word, charIndex, wordindex, node, palindromes):
            
            #If the first character of the 
            if charIndex < len(word) and word[charIndex] in node:
                updatePalindromes(word, charIndex+1, wordindex, node[word[charIndex]], palindromes)
            
            # We found a word that matches a prefix of the search word. We check that it's not the search word itself. e.g. ss could be matched with itself giving an incorrect result. 
            # We also check that the unmatched characters in the search word which will be between the matched characters form a palnindrome
            if "#" in node and node["#"] != wordindex and isPalindrome(word, charIndex, len(word)-1): 
                palindromes.append(node["#"])
            
            # We reached the end of current word while matching for pallindromes but there are additional characters left in the trie path. 
            # The unmatched trie will fall between the matched characters. We get all palindromes from the trie e.g. s and lls
            if charIndex>=len(word): 
                getPalindromesInTrieNode(node, palindromes)
                
        def getPalindromesInTrieNode(node, palindromes):
            # Do a BFS for each node in the node to get the list of pallindromes
            for ch in node:
                if ch != "#": # skip termination nodes
                    q = queue.deque()
                    q.append((ch,node[ch]))
                    while q:
                        currentWord, _node = q.popleft()
                        for key, val in _node.items():
                            if key == "#":
                                if isPalindrome(currentWord):
                                    palindromes.append(val)
                            else:
                                q.append((currentWord+key, val))
        
        out = []
        blankIdx = None
        for i, word in enumerate(words):
            if len(word) > 0:
                palindromes = [] 
                updatePalindromes(word, 0, i, t.nodes, palindromes)
                for x in palindromes:
                    out.append([i,x])
            else:
                blankIdx = i
        # Empty strings can be matched with all palindromes in the list
        if blankIdx is not None:
            for i, word in enumerate(words):
                if i != blankIdx and isPalindrome(word):
                    out.append([blankIdx, i])
                    out.append([i, blankIdx])
            
        return out
