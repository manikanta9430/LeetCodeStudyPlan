class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)   
      
        if n == 0: 
            return 0
    
        preDp = [0 for _ in range(n)]   
        
        for i in range(k):   
            dp = preDp[:] 
            maxi = -prices[0]  
			
            for j in range(1, n): 
                dp[j] = max(dp[j-1], dp[j], prices[j]+maxi) 
                maxi = max(maxi, preDp[j-1]-prices[j])  
				
            preDp = dp  
        
        return preDp[-1] 
