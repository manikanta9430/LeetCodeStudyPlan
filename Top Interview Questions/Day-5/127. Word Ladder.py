class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList = [beginWord]+wordList
        dic = {}
        size = len(beginWord)
        for word in wordList:
            for i in range(size):
                group = word[:i]+'*'+word[i+1:]
                dic[group] = ( dic[group]  if group in dic else []) + [word]        

        q = deque([beginWord])
        seen = set([beginWord])
        res = 0
        while len(q):
            for i in range(len(q)):
                current = q.popleft()
                if current==endWord:
                    return res+1
                for i in range(size):
                    group = current[:i]+'*'+current[i+1:]
                    for nei in dic[group]:
                        if nei not in seen:
                            q.append(nei)
                            seen.add(nei)
            res += 1
                    
        return 0
