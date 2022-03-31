class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ds = (s+s)[1:-1]
        print (ds)
        
        return s in ds
