class Solution:
    def canMeasureWater(self, jug1: int, jug2: int, target: int) -> bool:
        stack = [0]
        visit = set()
        while stack:
            water = stack.pop(0)
            if water<0 or water>jug1+jug2: continue
            if water in visit: continue
            visit.add(water)
            
            if water==target: return True
            stack.append(water+jug1)
            stack.append(water-jug1)
            stack.append(water+jug2)
            stack.append(water-jug2)
        return False
