class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        for i in range(m):
            summ=0
            for j in range(n):
                if matrix[j][i]!='0':
                    summ+=1
                    matrix[j][i]=summ
                else:
                    matrix[j][i]=0
                    summ=0
        maxx=0
        def maxArea(l):
            nonlocal maxx
            left=[]
            right=[]
            stack=[]
            for i,val in enumerate(l):
                while stack!=[] and l[stack[-1]] >= val:
                    stack.pop()
                if stack:
                    left.append(stack[-1]+1)
                else:
                    left.append(0)
                stack.append(i)
            stack=[]
            for i in range(len(l)-1,-1,-1):
                while stack!=[] and l[stack[-1]] >= l[i]:
                    stack.pop()
                if stack:
                    right.append(stack[-1]-1)
                else:
                    right.append(len(l)-1)
                stack.append(i)
            right=right[::-1]
            for i in range(len(l)):
                maxx=max(maxx,l[i]*(right[i]-left[i]+1))
        for i in matrix:
            maxArea(i)
        return maxx
