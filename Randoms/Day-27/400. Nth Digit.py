class Solution:
    def __init__(self):
        self.d = {1:9}
        while self.d[len(self.d)] < 2** 31 - 1:
            o_d = len(self.d)
            n_d = len(self.d) + 1
            self.d[n_d] = self.d[o_d] + 9 * (10 ** (n_d - 1)) * n_d
        self.d[0] = 0
            
    def findNthDigit(self, n: int) -> int:
        if n <= 9:
            return n
        #print(self.d)
        for x in range(1, 10):
            if self.d[x] >= n:
                low = x - 1
                digit = x
                break
        rem = (n - self.d[low])
        if rem % digit == 0:
            num = rem // digit + 10 ** (digit - 1) - 1
            return int(str(num)[-1])
        else:
            num = rem // digit + 10 ** (digit - 1)
            return int(str(num)[rem % digit - 1])
