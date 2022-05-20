class Solution(object):
    def wiggleSort(self, nums):
        for i, num in enumerate(sorted(nums, reverse=True)):
            if i < len(nums) // 2:  nums[2*i+1] = num
            else:   nums[len(nums)%2-2*(len(nums)-i)] = num
