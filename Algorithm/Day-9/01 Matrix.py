class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        q = deque()
        for x in range(m):
            for y in range(n):
                if mat[x][y] == 0:
                    q.appendleft((x, y))
                else:
                    mat[x][y] = -1 
        while q:
            x, y = q.pop()
            for r, c in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= r < m and 0 <= c < n and mat[r][c] == -1:
                    mat[r][c] = mat[x][y] + 1
                    q.appendleft((r, c))
        return mat
