class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       
        num_days = len(prices)
        dp = [[[0, 0], [0, 0]] for _ in range(num_days)]
        dp[0][0][1] = -prices[0]
        for i in range(1, num_days):
            dp[i][0][0] = max(dp[i-1][0][0], dp[i-1][1][0])
            dp[i][0][1] = max(dp[i-1][0][1], dp[i-1][0][0] - prices[i])
            dp[i][1][0] = dp[i-1][0][1] + prices[i]
        return max(dp[num_days - 1][0][0], dp[num_days - 1][1][0])
