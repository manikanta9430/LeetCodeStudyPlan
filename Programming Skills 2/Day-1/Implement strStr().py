class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        elif needle in haystack:
            result = haystack.index(needle)
            return result
        else:
            return -1
