class Solution:
    def isNumber(self, s: str) -> bool:
        if (len(s) >= 2
            and s[0] in {'+', '-'}
            and s[1] in {'E', 'e'}):
                return False
        if (('e' in s and 'E' in s) 
            or len(s.split('e')) > 2 
            or len(s.split('E')) > 2):
            return False
        if 'e' in s:
            ss = s.split('e')
        elif 'E' in s:
            ss = s.split('E')
        else:
            ss = [s, "0"]
        return (self.isDecimalOrInteger(ss[0]) 
                and self.isInteger(ss[1]))
    
    def isDecimalOrInteger(self, s):
        if self.isInteger(s):
            return True
        if not s:
            return False
        if s[0] == '+' or s[0] == '-':
            s = s[1:]
        if len(s.split('.')) > 2:
            return False
        if '.' in s:
            ss = s.split('.')
        else:
            ss = [s, "0"]
        if not ss[0] and not ss[1]:
            return False
        return ((not ss[0] 
                 or ss[0].isdigit()) 
                and 
                (not ss[1] 
                 or ss[1].isdigit()))
    
    def isInteger(self, s):
        if s and (s[0] in {'+', '-'}):
            s = s[1:]
        return s.isdigit()

