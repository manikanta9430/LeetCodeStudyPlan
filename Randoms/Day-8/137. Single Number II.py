class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = Counter(nums)
        return sorted(d, key=d.get)[0]
