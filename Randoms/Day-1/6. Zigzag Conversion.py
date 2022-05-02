class Solution(object):
    def convert(self, A, B):
        d = ["" for r in range(B + 1)]

        i = 0
        while (i < len(A)):
			# go downwards
            for j in range(1, B + 1):
                if (not i < len(A)): break
                d[j] += A[i]
                i += 1
			# go upwards
            for j in range(B - 1, 1, -1):
                if (not i < len(A)): break
                d[j] += A[i]
                i += 1
			#repeat
        ans = ''.join(d)
        return ans
