#MySolution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        least=min(prices)
        least_index=prices.index(least)
        
        pro=[]
        for i in prices[least_index+1:]:
            dif=i-least
            pro.append(dif)
    
        maxi_index=pro.index(max(pro))
        return least_index+maxi_index+2
      
#Submitted One:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxP = 0
        curP = 0
        for i in range(1,len(prices)):
            curP = curP + prices[i] - prices[i-1]
            if(curP<0):
                curP = 0
            maxP = max(maxP,curP)
        return maxP
