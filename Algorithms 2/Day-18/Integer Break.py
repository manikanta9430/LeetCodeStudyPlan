class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        res = collections.deque([1,1,2,0])
        for i in range(2, n-1):
            res[3] = max(2*res[1], 3*res[0], 2*i, 3*(i-1))
            res.rotate(-1)
        return res[2]
