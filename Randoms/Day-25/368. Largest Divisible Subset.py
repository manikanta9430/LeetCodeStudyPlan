class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        nums = sorted(nums) # sort to make sure if nums[j] % nums[i] == 0 for j > i then nums[j] % nums[k] == 0 for all nums[k] in dp[i] 
        dp = [[num] for num in nums]
        for i in range(1, len(nums)):
            for j in range(i):
                if not nums[i] % nums[j]:
                    if (len(dp[j]) + 1) > len(dp[i]):
                        dp[i] = dp[j] + [nums[i]]
        
        return max(dp, key=len)
