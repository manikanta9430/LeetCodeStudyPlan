class Solution:
    def minimumLines(self, A: List[List[int]]) -> int:
        A.sort() # to bring consecutive points on graph together
        n=len(A)
                
        # calculate if three points lie on the same line        
        is_same_line = lambda a,b,c: (b[0]-a[0])*(c[1] - b[1])==(c[0]-b[0])*(b[1] - a[1])
        
        return n - 1 - sum(is_same_line(A[i-1], A[i], A[i+1]) for i in range(1, n-1) )
