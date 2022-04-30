class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        @lru_cache(None)
        
        def helper(ind,target):
            if ind<0:
                return True if target==0 else False
            if target==0:
                return True
            if nums[ind]>target:
                return helper(ind-1,target)
            else:
                return helper(ind-1,target-nums[ind]) or helper(ind-1,target)
        
        s=sum(nums)
        if s&1==1:
            return False
        else:
            return helper(len(nums)-1,s//2)
