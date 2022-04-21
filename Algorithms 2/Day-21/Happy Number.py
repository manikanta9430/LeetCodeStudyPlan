class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1: return True
        l = []
        def calculate(n):
            c = 0
            for i in str(n):
                c += int(i) ** 2
            return c
        
        while n != 1:
            n = calculate(n)
            if n in l:
                return False
            l.append(n)
        return True
