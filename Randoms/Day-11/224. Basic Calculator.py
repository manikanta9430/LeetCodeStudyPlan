class Solution:
    def calculate(self, s: str) -> int:
        q = deque()
        for i in s:
            if i != ' ':
                q.append(i)
        q.append('+')
        return self.cal(q)
    
    
    def cal(self,q):
        stack = []
        runNum = 0
        sign = '+'
        
        while q:
            curChar = q.popleft()
            if curChar.isdigit():
                runNum = (runNum*10) +int(curChar)
            elif curChar == '(':
                runNum = self.cal(q)
            else:
                if sign == '+':
                    stack.append(runNum)
                elif sign == '-':
                    stack.append(-runNum)
                        
                if curChar == ')':
                    return sum(stack)
                runNum = 0
                sign = curChar
                
                
        return sum(stack)
