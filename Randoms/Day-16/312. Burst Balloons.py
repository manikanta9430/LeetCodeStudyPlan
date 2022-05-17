class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        if(n == 1):
            return nums[0]
        nums.append(1)
        nums.insert(0,1)
        n+=2
        dp = [[0]*302 for i in range(302)]
        
        for left in range(n-2,0,-1):
            for right in range(left,n-1,1):
                for i in range(left,right+1):
                    current = nums[left-1]* nums[i]* nums[right+1]
                    remaining = dp[left][i-1]+dp[i+1][right]
                    dp[left][right] = max(dp[left][right],current+remaining)
        return dp[1][n-2]
