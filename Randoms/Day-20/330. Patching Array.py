class Solution(object):
    def minPatches(self, nums, n):
        count=0
        i=1
        while(i<=n):
            if len(nums)>0 and i<nums[0]:
                count+=1
                i=i*2
            elif len(nums)>0 and  i==nums[0]:
                i=i*2
                nums.pop(0)
            elif len(nums)>0 and  i>nums[0]:
                while len(nums)>0 and (i>nums[0]):
                    i=i+nums[0]
                    nums.pop(0)
            elif len(nums)==0:
                count+=1
                i=i*2
        return count
