class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        win_start = 0
        win_sum = 0
        min_len = 10000
        for win_end in range(len(nums)):
            win_sum += nums[win_end]
            while win_sum >= target:
                min_len = min(min_len, win_end - win_start + 1)
                win_sum -= nums[win_start]
                win_start += 1
        if min_len == 10000:
            return 0
        return min_len
