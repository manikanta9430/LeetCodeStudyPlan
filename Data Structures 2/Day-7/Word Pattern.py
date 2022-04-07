class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d={}
        l=list(s.split(" "))
        
        if len(l)!= len(pattern):
            return False 
        
        if len(set(l))!=len(set(pattern)):
            return False
        
        for i in range(len(l)):
            if pattern[i] not in d:
                d[pattern[i]]= l[i]
                
            elif d[pattern[i]]!=l[i]:
                return False
            
        return True
