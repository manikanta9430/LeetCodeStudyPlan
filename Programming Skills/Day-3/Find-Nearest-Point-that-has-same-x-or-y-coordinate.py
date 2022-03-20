class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        mdist=float('inf')
        index = -1
        for i in range(len(points)):
            if(points[i][0] == x or points[i][1]== y):
                num = abs(x-points[i][0])+abs(y-points[i][1])
                if num<mdist:
                    mdist = num
                    index = i
        return index
