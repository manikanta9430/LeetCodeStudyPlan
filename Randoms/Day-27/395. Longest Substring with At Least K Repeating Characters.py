class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res = -inf
        for u in range(1, len(set(s)) + 1):
            l = 0
            c = Counter()
            for r in range(len(s)):
                c[s[r]] += 1
                if r - l + 1 < k or len(c) < u:
                    continue
                elif len(c) > u:
                    while l < r and len(c) > u:
                        c[s[l]] -= 1
                        if c[s[l]] <= 0:
                            del c[s[l]]
                        l += 1
                if len(c) == u:
                    if all([c[ch] >= k for ch in c]):
                        res = max(res, r - l + 1)
        return max(res, 0)
