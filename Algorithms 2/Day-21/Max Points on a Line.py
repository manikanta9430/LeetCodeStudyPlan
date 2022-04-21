import math

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return len(points)
        
        def getdxy(cord1, cord2):
            # output unqiue dx dy
            dx = cord1[0] - cord2[0]
            dy = cord1[1] - cord2[1]
            if dx == 0:
                return math.inf
            else:
                return dy / dx
        
        lined = set()
        maxlen = 2
        for idx in range(len(points)):
            if idx not in lined:
                directions = defaultdict(int)
                for nidx in range(idx+1, len(points)):
                    if nidx != idx:
                        dxy = getdxy(points[idx], points[nidx])
                        directions[dxy] += 1
                        maxlen = max(maxlen, directions[dxy]+1)
                        if directions[dxy] > 2:
                            lined.add(nidx)
        return maxlen
