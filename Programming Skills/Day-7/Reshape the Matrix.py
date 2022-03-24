class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n, count = len(mat), len(mat[0]), 0
        if m*n != r*c: return mat
        res = [[0] * c for _ in range(r)]
        for i, j in product(range(m), range(n)):
            res[count//c][count%c] = mat[i][j]
            count += 1      
        return res
