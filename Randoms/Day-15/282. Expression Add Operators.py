class Solution:
    
    def evaluate(self, a, b, op):
        if op == "+":
            return a+b
        elif op == "-":
            return a-b
        elif op == "*":
            return a*b
    
    def backtrack(self, num_arr, operations):
        if len(operations) == len(num_arr)-1:
            op_stack = []
            num_stack = [num_arr[0]]
            for i in range(1, len(num_arr)):
                while(op_stack and i-1>0 and self.priority[op_stack[-1]]>=self.priority[operations[i-1]]):
                    o = op_stack.pop()
                    b = num_stack.pop()
                    a = num_stack.pop()
                    num = self.evaluate(a, b, o)
                    num_stack.append(num)
                else:
                    op_stack.append(operations[i-1])
                    num_stack.append(num_arr[i])
            while(op_stack):
                o = op_stack.pop()
                b = num_stack.pop()
                a = num_stack.pop()
                num = self.evaluate(a, b, o)
                num_stack.append(num)    
            if num_stack[-1]==self.target:
                tmp_res = ""
                for i, n in enumerate(num_arr):
                    tmp_res+=str(num_arr[i])
                    if i<len(operations):
                        tmp_res+=operations[i]
                self.res.append(tmp_res)
            return
        
        operations.append("+")
        self.backtrack(num_arr, operations)
        operations.pop()

        operations.append("-")
        self.backtrack(num_arr, operations)
        operations.pop()

        operations.append("*")
        self.backtrack(num_arr, operations)
        operations.pop()
    
    def backtrackNum(self, num, status):
        if len(status) == len(num)-1:
            current = num[0]
            tmp_res = []
            for i in range(1, len(num)+1):
                if len(current)>1 and current[0] == "0":
                    return
                if i == len(num):
                    tmp_res.append(int(current))
                elif status[i-1] != 0:
                    tmp_res.append(int(current))
                    current = num[i]
                else:
                    current+=num[i]

            self.num_arr_total.append(list(tmp_res))
            return
                
        status.append(0)
        self.backtrackNum(num, status)
        status.pop()
        status.append(1)
        self.backtrackNum(num, status)
        status.pop()
    
    def addOperators(self, num: str, target: int) -> List[str]:
        self.target = target
        self.priority = 

{"+":0, "-":0, "*":1}
        self.num_arr_total = []
        self.res = []
        self.backtrackNum(num, [])
        #print(self.num_arr_total)
        for num_arr in self.num_arr_total:
            self.backtrack(num_arr, [])
        return self.res
