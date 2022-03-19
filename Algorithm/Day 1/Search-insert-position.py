class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        nu =[x for x in nums if x<target]
        return len(nu)
