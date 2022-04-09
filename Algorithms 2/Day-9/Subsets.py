class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = list()
        n = len(nums)
        
        def helper(l, c):
            nonlocal n
            result.append(l)
            if c == n:
                return
            i = c
            while i < n:
                helper([*l, nums[i]], i+1)
                i += 1
                
        helper([], 0)
        
        return result
