class Solution:
    def countDigitOne(self, n: int) -> int:
        '''
		reference : https://www.youtube.com/watch?v=ZOMKUPHcNRI
		consider countDigitOne as f, so countDigitOne(9) = f(9)
		
        13
        1*f(9)
        
        234
        2*f(99) (because 0-99, 200-299)
        + 100 count of 1s (100-199) since first digit from left is 2 which is > 1 
        + f(34)
        
        134
        1*f(99) 
        + rem=35 count of 1s (100-134) since first digit 1 == 1 
        + f(34)
        '''
		
        if n == 0: return 0
        if n <= 9: return 1
        ans = 0
        
        dp = {}
        dp[9] = 1
        i = 9
        while i <= n:
            # dp[i]* 10 because there will be 10 such places where dp[i]
            # will be repeated. 
            # consider, i = 99 , 10*i + 9 = 999 
            # 0-99 is repeated 10 times, 0-99 , 100-199, 900-999
            # (i+1) because
            # first digit 1 comes in 100-199 , 99+1 times
            dp[10*i + 9] = dp[i]*10 + (i+1)
            i = 10*i + 9
    
        # get first digit from left 
        max10baseddivisor = 1
        tmp = n
        while tmp//10 > 0:
            tmp = tmp//10
            max10baseddivisor*=10 
        
        firstdigit = n // max10baseddivisor
        ans += firstdigit*dp[max10baseddivisor - 1]
        rem = n % max10baseddivisor
        
        if firstdigit == 1:
            ans += rem + 1
        else:
            ans += max10baseddivisor
            
        ans += self.countDigitOne(rem)
        return ans
