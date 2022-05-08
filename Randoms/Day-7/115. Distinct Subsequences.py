class Solution:
    def numDistinct(self, s1: str, s2: str) -> int:
        n1 = len(s1)
        n2 = len(s2)
        dp = [[-1 for _ in range(n2)] for _ in range(n1)]
        def rec(i1, i2):
            if i2 >= n2: return 1
            if i1 >= n1: return 0
            if dp[i1][i2] == -1:
                c1 = c2 = 0
                if s1[i1] == s2[i2]:
                    c1 = rec(i1+1, i2+1)
                c2 = rec(i1+1, i2)
                dp[i1][i2] = c1 + c2
            return dp[i1][i2]
        return rec(0, 0)
