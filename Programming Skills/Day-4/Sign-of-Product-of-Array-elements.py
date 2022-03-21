class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for x in nums:
            product *= x
        if(product>0):
            return 1
        if(product<0):
            return -1
        return 0
