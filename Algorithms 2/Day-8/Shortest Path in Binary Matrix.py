class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0]:
            return -1
        
        q = deque([(0, 0, 0)])
        while q:
            x, y, d = q.popleft()
            
            if x == n-1 and y == n-1:
                return d + 1
            
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                newx, newy = x + dx, y + dy
                
                if 0 <= newx < n and 0 <= newy < n and not grid[newx][newy]:
                    grid[newx][newy] = 1
                    q.append((newx, newy, d + 1))
                    
        return -1
