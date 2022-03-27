class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        total=sum(grid[i][j]==1 for i in range(len(grid)) for j in range(len(grid[0])))
        if total==0: return 0
        deque=collections.deque([(i,j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j]==2])
        cur=0
        while deque:
            for _ in range(len(deque)):
                i,j=deque.popleft()
                possible=[(x,y) for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)] if 0<=x<len(grid) and 0<=y<len(grid[0])]
                for x,y in possible:
                    if grid[x][y]==1:
                        grid[x][y]=2
                        total-=1
                        deque.append((x,y))
            cur+=1
            if total==0: return cur
        return cur if total==0 else -1
