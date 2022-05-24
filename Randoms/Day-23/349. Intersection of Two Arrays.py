class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        rec = {}
        intersection = {}
        
        for num in nums1:
            rec[num] = True

        for num in nums2:
            if num in rec:
                intersection[num] = True
        
        return list(intersection.keys())
