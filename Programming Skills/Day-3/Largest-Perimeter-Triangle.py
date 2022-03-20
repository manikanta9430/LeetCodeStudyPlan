class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums)<3: return 0
        nums.sort(reverse=True)
        a,b=nums[:2]
        for c in nums[2:]:
            if b+c>a:
                return a+b+c
            a,b=b,c
        return 0
