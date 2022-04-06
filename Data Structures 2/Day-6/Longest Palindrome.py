class Solution:
    def longestPalindrome(self, s: str) -> int:
        return min(sum([(x//2)*2 for x in Counter(s).values()])+1, len(s))

