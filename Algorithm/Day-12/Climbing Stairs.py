class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        k = [None]*n
        k[0] = 1
        k[1] = 2
        
        for i in range(2,n):
            k[i] = k[i-1]+k[i-2]
        return k[n-1] 		
