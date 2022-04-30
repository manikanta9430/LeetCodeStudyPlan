class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            res.append(sum(map(int,(format(i,"b")))))
        return res
