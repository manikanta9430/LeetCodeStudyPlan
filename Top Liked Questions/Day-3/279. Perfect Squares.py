from math import floor, sqrt


class Solution:
    
    def numSquares(self, n: int) -> int:
        
        @lru_cache(None)
        def helper(n: int) -> int:
            if n == 0:
                return 0

            r = range(1, floor(sqrt(n)) + 1)
            return min(helper(n - i*i) for i in r) + 1
        
        return helper(n)
