class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        operFunc = {"+": add, "-": sub, "*": mul}
        memo = {}
        def helper(expr: str) -> List[int]:
            if expr in memo:
                return memo[expr]

            if len(expr) <= 2:
                memo[expr] = [int(expr)]
                return memo[expr]

            ans = []
            for i in range(len(expr)):
                if expr[i] in operFunc:
                    arg1List = helper(expr[:i])
                    op = expr[i]
                    arg2List = helper(expr[i+1:])
                    ans += [operFunc[op](arg1, arg2)
                            for arg1 in arg1List
                            for arg2 in arg2List
                           ]
            memo[expr] = ans
            return ans

        return helper(expression)
