class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = []
        max_length = 0
        
        #first loop: i is the center of palindromic string (odd length)
        for i in range(1,len(s)-1): 
            temp = 0
            for j in range( 1, min(i, len(s)-1-i) + 1 ):
                if s[i-j] != s[i+j]:
                    break
                temp += 1
            if 2*temp + 1 > max_length:
                max_length = 2*temp + 1 
                result = s[i-temp:i+temp+1]

        #second loop: the center of palindromic string is between i-1 and i (even length)   
        for i in range(1,len(s)): 
            temp = 0
            for j in range( 1, min(i, len(s)-i) + 1  ):
                if s[i-j] != s[i+j-1]:
                    break
                temp += 1
            if 2*temp > max_length:
                max_length = 2*temp  
                result = s[i-temp:i+temp]
        
        if max_length == 0:       #check if trivial solution with only one element
            return s[0]
        return result
