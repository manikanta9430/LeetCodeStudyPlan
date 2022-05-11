class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        
        m_idx = (len(s)-1)//2
        
        while m_idx>=0:
            middle_char = s[m_idx]
            l_idx = m_idx-1
            r_idx = m_idx+1
            
            while (r_idx <= len(s)-1 and s[r_idx]==middle_char) or (l_idx>=0 and s[l_idx]==middle_char):
                
                if (l_idx>=0 and s[l_idx]==middle_char):
                    l_idx-=1
                if (r_idx <= len(s)-1 and s[r_idx]==middle_char):
                    r_idx-=1
            
            left = s[:l_idx+1]
            middle = s[l_idx+1:r_idx] 
            right = s[r_idx:]
            
            if not left or left[::-1] == right[:len(left)]:
                return right[::-1] + s[l_idx+1:]
            
            m_idx = l_idx
