class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if(n==0):
            return 0
        if(n == 1):
            return nums[0]
        curr =0
        maxi = nums[0]
        for num in nums:
            curr = max(num,curr+num)
            maxi = max(maxi,curr)
        return maxi
    
    
            
