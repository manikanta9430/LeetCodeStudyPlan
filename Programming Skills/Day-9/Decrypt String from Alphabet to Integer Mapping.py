class Solution:
    def freqAlphabets(self, s: str) -> str:
        j = len(s)-1
        
        ans = ''
        
        while j >= 0:
            if s[j] == '#':
                ans += str(chr(ord('a')+int(s[j-2:j])-1))
                j-=3
            else:
                ans += str(chr(ord('a')+int(s[j])-1))
                j-=1

        return ans[::-1]
