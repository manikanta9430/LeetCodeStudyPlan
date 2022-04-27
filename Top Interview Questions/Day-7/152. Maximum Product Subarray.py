class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        dp = 1
        min_ = max_ = 1
        max_val = nums[0]
        for i in range(len(nums)):
            if nums[i] == 0:
                min_ = max_ = 1
                dp = 1
                max_val = max(max_val, 0)
                continue
                
            current_mul = nums[i]*dp
            if current_mul >=0:
                max_val = max(max_val, current_mul)
            else:
                if min_>=0 and max_>=0:
                    max_val = max(max_val, current_mul//max_)
                if min_<0 and max_>=0:
                    max_val = max(max_val, current_mul//min_)
                if min_<0 and max_<0:
                    max_val = max(max_val, current_mul//max_)
            if min_<0 and current_mul<0:
                min_ = max(min_, current_mul)
            else:
                min_ = min(min_, current_mul)
            max_ = max(max_, current_mul)
            dp = current_mul
            
        return max_val
