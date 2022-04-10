class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        res = 0
        left, right = 0, 0
        product = 1
        while right < len(nums):
            
            product *= nums[right]
            while left <= right and product >= k:
                product /= nums[left]
                left += 1
            
            res += right - left + 1
            right += 1
            
        return res
