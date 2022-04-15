class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
		n = len(s)
        word_set = set(wordDict)
        word_length = [len(x) for x in wordDict]
        min_length, max_length = min(word_length), max(word_length)
		
        if len(s) < min_length:
            return False
        
		dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n - min_length + 2):
            for j in range(i - 1 + min_length, min(i + max_length, n + 1)):
                if dp[i - 1] and s[i - 1:j] in word_set:
                    dp[j] = True
        return dp[-1]
