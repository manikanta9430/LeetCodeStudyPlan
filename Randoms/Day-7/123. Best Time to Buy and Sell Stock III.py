class Solution:
    def maxProfit(self, prices: List[int]) -> int:    
        l = len(prices)
        
        # Calculate p1:
        p1 = [0 for _ in range(l)]
        min_ = prices[0]
        for i in range(1, l):
            if prices[i] < min_:
                min_ = prices[i]                
            p1[i] = max(p1[i-1], prices[i] - min_)
            
        
        # Calculate p2:
        p2 = [0 for _ in range(l)]
        max_ = prices[l-1]
        for i in range(l-2, -1, -1):
            if prices[i] > max_:
                max_ = prices[i]
            p2[i] = max(max_ - prices[i], p2[i+1])
            

        p = [x + y for x, y in zip(p1, p2)]
        return max(p)
