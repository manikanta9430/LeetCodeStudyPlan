class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        return [i for i, v in Counter(nums).items() if v > len(nums)/3]
