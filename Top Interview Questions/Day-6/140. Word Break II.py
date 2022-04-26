class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        def helper(string, path):
            if string == "":
                return result.append(" ".join(path))
 
            for word in wordDict:
                if string.startswith(word):
                    wordlen = len(word)
                    helper(string[wordlen:], path + [word])
        
        result = []
        helper(s, [])
        return result
