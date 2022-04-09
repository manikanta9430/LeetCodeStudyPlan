class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        DNA_set = set()
        seen = set()
        start = 0
        end = 9 
        
        while end < len(s):
            if s[start:end+1] not in seen:
                seen.add(s[start:end+1])
            else:
                DNA_set.add(s[start:end+1]) 
            
            end += 1
            start += 1
            
        return list(DNA_set)
