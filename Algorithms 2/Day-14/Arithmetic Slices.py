class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        
        
        diff_arr = [0]*(len(nums)-1)
        dict_arr = defaultdict(int)
        
        for i in range(1,len(nums)):
            diff_arr[i-1] = nums[i]-nums[i-1]
            
            
        ans = 0
        count_sum = 1
        
        for i in range(1,len(diff_arr)):
            
            if diff_arr[i] == diff_arr[i-1]:
                ans += count_sum
                count_sum += 1
            else:
                count_sum = 1
                
        return ans
