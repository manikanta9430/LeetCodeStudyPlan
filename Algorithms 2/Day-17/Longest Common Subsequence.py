class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        def sub(text1, text2, n1, n2):
            dp = [0] * (n2 + 1)
            for i in range(n1):
                newdp = [0] * (n2 + 1)
                for j in range(n2):
                    if text1[i] == text2[j]:
                        newdp[j + 1] = 1 + dp[j]
                    else:
                        newdp[j + 1] = max(dp[j + 1], newdp[j])
                dp = newdp
            return dp[n2]
        if n1 > n2:
            return sub(text1, text2, n1, n2)
        else:
            return sub(text2, text1, n2, n1)
