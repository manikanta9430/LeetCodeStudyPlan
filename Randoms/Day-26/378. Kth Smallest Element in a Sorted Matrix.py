class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        N = len(matrix)
        for i in range(1, N):
            for j in range(N):
                matrix[0].append(matrix[i][j])
        matrix[0].sort()

        return matrix[0][k-1]
