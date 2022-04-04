class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[None] * n for _ in range(n)]
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        steps = [n, n - 1]
        num = 1
        dir = 0
        x = 0
        y = -1
        while steps[dir % 2] > 0:
            for _ in range(steps[dir % 2]):
                x += dirs[dir][0]
                y += dirs[dir][1]
                matrix[x][y] = num
                num += 1
            steps[dir % 2] -= 1
            dir = (dir + 1) % 4
        return matrix
