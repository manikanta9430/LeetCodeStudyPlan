class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        # dirs = [up, right, down, left]
        dirs = [(-1,0), (0,1), (1,0), (0,-1)]
        rows, cols = len(matrix), len(matrix[0])
        
        def dfs(r, c, direction):
            seen.add((r,c))
            traverse.append(matrix[r][c]) # preorder traversal
            for i in range(4):
                new_direction = (direction + i) % 4
                nr = r + dirs[new_direction][0]
                nc = c + dirs[new_direction][1]
                if nr < 0 or nc < 0  or nr >= rows or nc >= cols or (nr, nc) in seen:
                    continue    
                dfs(nr, nc, new_direction)
                
        seen = set()
        traverse = []
        dfs(0, 0, 1)
        return traverse
