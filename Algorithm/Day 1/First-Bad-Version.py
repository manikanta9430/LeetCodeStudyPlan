class Solution:
    def firstBadVersion(self, n: int) -> int:
        l,r = 0,n
        m = l+(r-l)//2
        while l<=r:
            if isBadVersion(m):
                r=m-1
            else:
                l = m+1
            m = l+(r-l)//2
        return l
