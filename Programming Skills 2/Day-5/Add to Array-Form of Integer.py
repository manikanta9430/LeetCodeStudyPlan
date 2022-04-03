class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s=""
        for i in num:
            s += str(i)
        s = int(s)
        s += k
        s = str(s)
        res=[]
        for l in s:
            res.append(l)
        return res
