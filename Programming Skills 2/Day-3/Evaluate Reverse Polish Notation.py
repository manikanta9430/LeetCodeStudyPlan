class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in tokens:
            if(i[-1].isnumeric()):
                stack.append(int(i))
            else :
                b=stack.pop()
                a=stack.pop()
                val=0
                if(i=="+"): val=a+b
                elif(i=="-"): val=a-b
                elif(i=="*"): val=a*b
                else: val=int(a/b)
                stack.append(val)
        return stack[0]
