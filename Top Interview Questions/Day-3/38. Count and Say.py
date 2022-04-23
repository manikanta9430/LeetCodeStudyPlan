class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(n - 1):
            s = ''.join(str(sum(1 for _ in j)) + str(i) for i,j in groupby(s))
        return s
