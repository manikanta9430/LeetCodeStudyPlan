class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        string_x = str(x)
        
        reversed_string_x = string_x[::-1]
        
        return string_x == reversed_string_x
