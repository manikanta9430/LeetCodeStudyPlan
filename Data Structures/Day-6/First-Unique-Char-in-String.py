class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters='abcdefghijklmnopqrstuvwxyz'
        ind = [s.index(l) for l in letters if s.count(l) == 1]
        return min(ind) if len(ind) >0 else -1
