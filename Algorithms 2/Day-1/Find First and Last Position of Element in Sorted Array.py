class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
    
        result  = [-1, -1]   
        
        def searchRangeRecurse(lo, hi):
            if lo>hi:
                return
            
            mid = lo + (hi-lo)//2   # integer division
            
            if target == nums[mid]:
                if result[0]==-1 or result[0] > mid:   # if target index is less than the first found index so far, update the first
                    result[0] = mid
                    
                if result[1] == -1 or result[1] < mid:   # if target index is grreater than the last found index so far, update the last
                    result[1] = mid
            
			# search in both direction to find all targets in the array
            searchRangeRecurse(lo, mid-1)
            searchRangeRecurse(mid+1, hi)
              
        searchRangeRecurse(0, len(nums)-1)
        return result
