class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1, prev2 = 0, 0
     
        for i in range(len(nums)):
            tmp = prev1
            prev1 = max(prev2 + nums[i], prev1)
            prev2 = tmp
        return prev1
