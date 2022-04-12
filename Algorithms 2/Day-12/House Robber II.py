def rob_from(position: int, end: int, nums: List[int], cache: dict[int, int]):
    if len(nums) == 1:
        return nums[0]

    if position >= end:
        return 0
    
    if position not in cache:
        cache[position] = max(
            rob_from(position + 1, end, nums, cache),
            nums[position] + rob_from(position + 2, end, nums, cache),
        )

    return cache[position]

class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(
            rob_from(0, len(nums) - 1, nums, {}),
            rob_from(1, len(nums), nums, {}),
        )
