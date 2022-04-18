class Solution:
    def minDistance(self, s: str, t: str) -> int:
        dp = defaultdict(lambda: defaultdict(int))
        def get_dp(ps, pt):
            nonlocal dp
            if dp[ps][pt]:
                return dp[ps][pt]
            if ps == len(s) and pt == len(t):
                dp[ps][pt] = 0
            elif ps == len(s) and pt < len(t):
                dp[ps][pt] = len(t) - pt #remove remaining characters of t
            elif ps < len(s) and pt == len(t):
                dp[ps][pt] = len(s) - ps #remove remaining characters of s
            else:
                if s[ps] != t[pt]:
                    dp[ps][pt] = 1 + min(get_dp(ps+1, pt + 1), get_dp(ps, pt+1), get_dp(ps+1, pt))
                else:
                    dp[ps][pt] = get_dp(ps+1, pt+1)
            return dp[ps][pt]
        return get_dp(0, 0)
