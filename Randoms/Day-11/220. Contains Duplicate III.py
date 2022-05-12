class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        
        buckets = {}
        # increment by one in case t is 0 (we need to divide by a non-zero number to find the key aka "label" in the article)
        w = t + 1
        for i, num in enumerate(nums):
            key = num//w
			
			# We found another element within t counts away that's stored in this bucket range
            if key in buckets:
                return True
            
			# We found another element that is stored in the prevous bucket
            if key - 1 in buckets and abs(num - buckets[key-1]) < w:
                return True
				
			# We found another element that is stored in hte next bucket
            if key + 1 in buckets and abs(num - buckets[key + 1]) < w:
                return True
            
            buckets[key] = num
            
			# remove the left-most element of the sliding window
            if i >= k:
                bKey = nums[i - k]//w
                del buckets[bKey]
                
        return False
