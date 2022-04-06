from numba import jit
@jit(nopython=True)

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        length = len(isConnected)
        visited = set()
        queue = []
        def bfs(row):
            queue = [row]
            while queue:
                current = queue.pop(0)
                visited.add(current)
                for j in range(length):
                    if isConnected[current][j] == 1 and j not in visited:
                        queue.append(j)
            
        count = 0
        for i in range(length):
            if i not in visited:
                bfs(i)
                count +=1
        
        return count
