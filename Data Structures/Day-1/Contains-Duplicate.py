class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        if(n == 0 or n == 1): return False
        for i in range(n):
            if(nums[i-1]==nums[i]): return True
        return False
