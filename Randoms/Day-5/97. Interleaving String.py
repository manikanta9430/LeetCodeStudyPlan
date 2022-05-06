class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        stack = [(0,0,0)]
        seen = {(0,0,0)}
        while stack:
            (i,j,k) = stack.pop()
            if k == len(s3) and i == len(s1) and j == len(s2):
                return True
            if i < len(s1) and k < len(s3) and s1[i] == s3[k] and (i+1, j, k+1) not in seen:
                stack.append((i+1, j, k+1))
                seen.add((i+1, j, k+1))
            if j < len(s2) and k < len(s3) and s2[j] == s3[k] and ( i, j+1, k+1) not in seen:
                stack.append(( i, j+1, k+1))
                seen.add(( i, j+1, k+1))
        return False
