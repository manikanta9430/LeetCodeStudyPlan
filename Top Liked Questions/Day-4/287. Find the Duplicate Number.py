class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        z=collections.Counter(nums)
        return z.most_common(1)[0][0]
