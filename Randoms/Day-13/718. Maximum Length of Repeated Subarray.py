class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # sliding window solution
        # 0. states:
        # a) start sliding position
        # A: [1,2,3,2,1]
        # B:         [3,2,1,4,7]
        # b) end sliding position
        # A:         [1,2,3,2,1]
        # B: [3,2,1,4,7]
        # c. total sliding positions: m + n - 1
        
        # 1. common subarray indices
        # a) i = 0, start_A = max(0, m-1-i) = m-1 (i.e., A starts with the last element)
        # A: [1,2,3,2,1]
        #    i = 0, start_B = max(0, i -(m-1)) = 0 (i.e., B starts with the first element)
        # B:         [3,2,1,4,7]
        
        # b) i = 5, start_A = max(0, m-1-5) = 0 (i.e., A starts with the first element)
        # A:          [1,2,3,2,1]
        #    i = 5, start_B = max(0, i-m+1) = 1 (i.e., B starts with the second elment)
        # B:        [3,2,1,4,7]
        
        # c) i = m+n-2, start_A = max(0, m-1-(m+n-2)) = 0 (i.e., A starts with the first element) 
        # A:         [1,2,3,2,1]
        #    i = m+n-2, start_B = max(0, m+n-2-(m-1)) = n-1 (i.e., B starts with the last element)
        # B: [3,2,1,4,7]
        
        # 2. iterative relation
        # at each state, 
        # a) if nums1[start_A] == nums2[start_B]: increment start_A, start_B, length_common_subarray, 
        # b) if nums1[start_A] != nums2[start_B]: reset current length_common_subarray, keep incrementing start_A and start_B
        m, n = len(nums1), len(nums2)
        maxLength = 0
        for i in range(0, m+n-1):
            start_A = max(0, (m-1) - i)
            start_B = max(0, i - (m-1))
            counter = 0
            while start_A < m and start_B < n:
                # note that we need to iterate the whole overlapping array becasue the first element of common
                # subarray may appear later
                if nums1[start_A] == nums2[start_B]:
                    counter += 1
                    maxLength = max(maxLength, counter)
                else:
                    counter = 0
                
                start_A += 1
                start_B += 1
        
        return maxLength
