class Solution(object):
    def findMin(self, nums):
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        if nums is None or n == 0:
            return

        start, end = 0, n - 1

        while start <= end:
            mid = (start + end) // 2
            
            if mid < end and nums[mid + 1] < nums[mid]:
                return nums[mid + 1]

            if mid > start and nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[start] <= nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid - 1

        return nums[start]
