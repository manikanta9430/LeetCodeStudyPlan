class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #Inilitiaze both sell and buy state
        sell_state, buy_state = 0, -float('inf')
        
        # Keep updating the max sell/rest and buy state after each day
        for price in prices:
            # Restore previous day sell/rest state to be used in 2 cases:
            # 1. To update current sell/rest state: whether to sell stock today or no
            # 2. To update current buy state: whether to buy stock today or no
            
            prev_sell_state = sell_state
            
            # To sell stock means going from buy state to sell by adding price to it
            sell_state = max(prev_sell_state, buy_state + price)
            # To buy stock means going from prev sell/rest state to buy state by subtracting price from it
            buy_state = max(buy_state, prev_sell_state - price)
            
            
        return max(sell_state, buy_state)
