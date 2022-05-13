class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        def helper(l, r):
            if l == r:
                return str(l)
            return str(l) + "->" + str(r)
        
        if len(nums) == 0:
            return []
        
        l = nums[0]
        r = nums[0]
        ret = []
        for i in range(1, len(nums)):
            if nums[i] == r + 1:
                r = nums[i]
            else:
                ret.append(helper(l, r))
                l, r = nums[i], nums[i]
            #print (ret)
        ret.append(helper(l, r))
        
        return ret

