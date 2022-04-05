class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        m = len(mat) -1 
        one = two = three = four = True
        for i in range(len(mat)):
            for j in range(len(mat[0])):

                if target[i][j] != mat[i][j]:
                    one = False

                if target[i][j] !=mat[m-j][i]:
                    two = False

                if target[i][j] !=mat[m-i][m-j]:
                    three = False

                if target[i][j] != mat[j][m-i]:
                    four = False

        return one | two | three | four
