class Solution:
    def complement(self, char):
        if char == ')':
            return '('
        if char == ']':
            return '['
        if char == '}':
            return '{'

    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '[' or char == '(' or char == '{':
                stack.append(char)
            elif char == ']' or char == ')' or char == '}':
                if len(stack) == 0:
                    return False
                val = stack.pop()
                if val != self.complement(char):
                    return False
        if len(stack) != 0:
            return False
        return True
