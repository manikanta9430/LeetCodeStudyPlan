class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        size = len(nums)
        
        # Answer to "Find Minimum in Rotated Sorted Array II"
            # ..with a slight modification
        l, r = 0, size - 1
        while l < r:
            m =  l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m 
            else:
                r -= 1 # decrement right boundary until one of the above 
                       # conditions is true
                # edge case 1: [1,1,1,1,1,1,2,1,1,1], target = 2
                # edge case 2: [1,1,2,1,1,1,1,1,1,1], target = 2
                if nums[r] == target:
                    return True
        pivot = l
        
        # It turns out that vanilla binary search can be performed,
            # with the only difference being instead of returning
            # the index if target is found, we return "True". Otherwise
            # we return "False"
        def binary_search(l, r):
            while l <= r:
                m = l + (r - l) // 2
                if nums[m] == target:
                    return True
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return False
        
        # Choosing which side to search on (solution to 
        #   "Search in Rotated Sorted Array")
        if nums[pivot] <= target <= nums[size - 1]:
            return binary_search(pivot, size - 1)
        else:
            return binary_search(0, pivot - 1)
