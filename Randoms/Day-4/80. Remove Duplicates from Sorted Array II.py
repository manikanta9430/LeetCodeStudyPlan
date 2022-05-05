from collections import Counter


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        for num, cnt in sorted(Counter(nums).items(),
                               key=lambda x: x[0]):
            move = min(cnt, 2)
            nums[idx:idx+move] = [num]*move
            idx += move
        return idx
