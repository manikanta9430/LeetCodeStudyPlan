from math import log

class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        x = pow(2, a)
        y = pow(2, b)
        z = x * y
        return int(log(z, 2))
