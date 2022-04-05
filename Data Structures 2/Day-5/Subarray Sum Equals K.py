class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        my_dict = {}
        pre_sum = 0
        count = 0
        for i in range(len(nums)):
            pre_sum += nums[i]
            if pre_sum == k:
                count += 1
            if (pre_sum-k) in my_dict:
                count += my_dict[pre_sum-k]
            if (pre_sum) not in my_dict:
                my_dict[pre_sum] = 1
            else:
                my_dict[pre_sum] += 1
        return count

