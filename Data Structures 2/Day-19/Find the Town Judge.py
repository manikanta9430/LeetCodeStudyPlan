class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n == 1:
            return 1
        elif not trust:
            return -1
        
        judgeCnt = Counter([ y for x, y in trust]).most_common()[0]
        
        if judgeCnt[1] != n - 1 or judgeCnt[0] in [ x for x, y in trust]:
            return -1
        
        return judgeCnt[0]
