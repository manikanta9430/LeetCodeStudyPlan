class Solution:
    
    def eval(self, num_stack, operator_stack):
        operator = operator_stack.pop()
        a = num_stack.pop()
        b = num_stack.pop()
        if operator == "+":
            num_stack.append(b+a)
        elif operator == "-":
            num_stack.append(b-a)
        elif operator == "*":
            num_stack.append(b*a)
        elif operator == "/":
            num_stack.append(b//a)
    
    def calculate(self, s: str) -> int:
        num_stack = []
        operator_stack = []
        num = ""
        num_set = set([str(i) for i in range(0, 10)])
        #priorities
        operator_map = {"+":0, "-":0, "*":1, "/":1}
        for i, c in enumerate(s):
            if c in num_set:
                num+=c
                if i == len(s)-1:
                    num_stack.append(int(num))
            else:
                if num!="":
                    num_stack.append(int(num))
                    num = ""
                if c in operator_map:
                    while len(operator_stack)>0 and operator_map[operator_stack[-1]] >= operator_map[c]:
                        self.eval(num_stack, operator_stack)
                    operator_stack.append(c)
        
        while len(operator_stack)>0:
            self.eval(num_stack, operator_stack)            

        return num_stack[-1]        
