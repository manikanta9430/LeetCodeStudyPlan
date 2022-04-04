class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        if N == 1:
            return
        flat = []
        for row in matrix:
            flat = flat + row
        out = [0] * len(flat)
        for n in range(N):
            outcol = N - 1 - n 
            col = flat[n * N: N * (n + 1)]
            out[outcol::N] = col
        for n in range(N):
            matrix[n] = out[n * N: N * (n + 1)]
