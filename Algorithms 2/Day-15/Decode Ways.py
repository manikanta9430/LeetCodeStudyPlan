class Solution:
    def numDecodings(self, s: str) -> int:
        vals=[str(i) for i in range(1,27)]
        n=len(s)
        dp=[0]*(n+1)
        dp[0]=1
        for i in range(1,n+1):
            if s[i-1] in vals:
                dp[i]+=dp[i-1]
            if i>1 and s[i-2:i] in vals:
                dp[i]+=dp[i-2]
        return dp[-1]
