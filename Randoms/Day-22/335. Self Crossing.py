class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        for i in range(len(distance)-2):
            # i cross i + 3
            if distance[i] >= distance[i+2] and i + 3 < len(distance) and distance[i+3] >= distance[i+1]:
                return True
            # i encounter i + 4
            elif i + 4 < len(distance) and distance[i+1] == distance[i+3] and distance[i] + distance[i+4] == distance[i+2]:
                return True
            # i cross i + 5
            elif i + 5 < len(distance) and 0 <= distance[i+3] - distance[i+1] <= distance[i+5] <= distance[i+3] and 0 <= distance[i+2] - distance[i] <= distance[i+4] <= distance[i+2]:
                return True
        return False
