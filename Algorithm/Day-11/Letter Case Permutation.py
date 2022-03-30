class Solution(object):
    def letterCasePermutation(self, s):
        arr = []
        
        def backTracking(subString):
            
            count = len(subString)
            
            if (count== len(s)):
                arr.append(subString)
                return
                
            if(s[count].isalpha()):
                backTracking(subString+s[count].swapcase())
                
            backTracking(subString +s[count])
            
        backTracking("")
        return arr
