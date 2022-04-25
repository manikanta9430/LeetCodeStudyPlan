class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward = ""
        backward = ""
        
        for i, j in zip(range(len(s)), range(len(s) -1, -1, -1)):
            if s[i].isalnum():
                forward += s[i].lower()
            if s[j].isalnum():
                backward += s[j].lower()                
                
        return forward == backward
