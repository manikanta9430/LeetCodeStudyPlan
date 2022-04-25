class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[0 for i in range(len(p)+1)] for i in range(len(s)+1)]
        dp[0][0] = 1
        for i in range(1, len(p)+1):
            curr = p[i-1]
            if curr == "*":
                dp[0][i] = dp[0][i-1]
        for r in range(1, len(s)+1):
            for c in range(1, len(p)+1):
                cs, cp = s[r-1], p[c-1]
                if cs == cp or cp == "?":
                    dp[r][c] = dp[r-1][c-1]
                elif cp == "*":
                    dp[r][c] = max(dp[r-1][c-1], dp[r-1][c], dp[r][c-1])
        return dp[len(s)][len(p)]
