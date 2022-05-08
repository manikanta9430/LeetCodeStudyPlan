class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
       # check if endword is in wordlist
        if endWord not in wordList:
            return []
        
        # insert a new value for the first time, the default value is an empty list
        nei = collections.defaultdict(list)
        
        wordList.append(beginWord)
        
        # build an adjacent list
        for word in wordList: # iterate each word
            for j in range(len(word)): # find patterns of each word
                pattern = word[:j] + "*" + word[j+1:] # replace the char in j position with *
                nei[pattern].append(word) # add the word in the dict
                
        # bfs
        visited = set([beginWord]) # don't visit the same word again
        q = deque()
        q.append((beginWord,[beginWord]))
        res  = []
        wordList = set(wordList)
        
        while q:
            # iterate layer
            for i in range(len(q)):
                word, seq = q.popleft()
                if word == endWord:
                    res.append(seq)
                
                # go with it's neighbors 
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    # check the neighbors
                    for neiWord in nei[pattern]:
                        # we don't check the word itself
                        if neiWord in wordList:
                            visited.add(neiWord)
                            q.append((neiWord, seq+[neiWord]))   
            wordList -= visited
        return res
