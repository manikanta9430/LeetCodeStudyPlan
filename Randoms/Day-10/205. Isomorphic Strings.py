class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        temp = dict()
        for i in range(len(s)):
            if s[i] not in temp:
                if t[i] in temp.values():
                    return False
                temp[s[i]] = t[i]
            else:
                if temp[s[i]] != t[i]:
                    return False
        return True
    
    
        
