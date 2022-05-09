class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        while left < right:
            
            mid = (left + right) // 2
            
            # here if we observe a improper order i.e nums[n] > nums[n - k]
            # then we can say that the pivot(smallest) lies in right partition
            if nums[mid] > nums[right]:
                left = mid + 1
            # here we check for the both ends since it might trick us with same values
            elif nums[left] != nums[right]:
                # the middle element could be the smallest element also , hence we don't 
                # ignore the middle element
                right = mid
            else:
                # if both the conditions failed it means both left and right ends are dups
                # so we can decrement right or increment the left so we ignore the duplicate
                # and reach the pivot(smallest) 
                left += 1 # right -= 1 also valid
            
        # after iteration the left element is supposedly carries the pivot(smallest) element
        return nums[left]
