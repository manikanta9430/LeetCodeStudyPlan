class Solution:
    def isUgly(self, n: int) -> bool:
        # Edge case
        if n == 0:
            return False
        # Keeps on dividing by 2, 3 and 5
        while n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
            if n % 2 == 0:
                n = n // 2
            elif n % 3 == 0:
                n = n // 3
            else:
                n = n // 5
        # n is expected to be 1 if it is an ugly number
        return n == 1
