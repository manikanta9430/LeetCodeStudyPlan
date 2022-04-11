class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parens = []
        def gp(n:int , op:int , cl:int , paren:str):
            if op < n:
                gp(n, op+1, cl, paren+"(")
                gp(n, op, cl+1, paren+")") if cl < op else None
            else:
                gp(n, op, cl+1, paren+")") if cl < op else parens.append(paren)
        gp(n, 0, 0, "")
        return parens
