class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        
        def find_k_max_number_in_an_array(nums, k):
            drop_possible = len(nums) - k
            n = len(nums)
            stack = []
            for i, val in enumerate(nums):
                while stack and drop_possible and stack[-1] < val:
                    drop_possible -= 1
                    stack.pop()
                
                stack.append(val)
            
            return stack[:k]
                
        
        def merge_two_array(arr1, arr2):
            #print(arr1, arr2)
            return [max(arr1, arr2).pop(0) for _ in arr1 + arr2]

        def compare_two_array(arr1, arr2):
            """
            determine whether arr1 is greater than arr2
            """
            if not arr2:
                return True
            i = j = 0
            n = len(arr1)
            while i < n and j < n:
                if arr1[i] > arr2[j]:
                    return True
                elif arr1[i] < arr2[j]:
                    return False
                i += 1
                j += 1
            
            return True
        
        ans = 0
        for i in range(k + 1):
            p = k - i
            
            if i > len(nums1) or p > len(nums2):
                continue
            
            # get this two array by solving function find_k_max_number_in_an_array
            # using similar concept of 402. Remove K Digits
            first_arr = find_k_max_number_in_an_array(nums1, i)
            second_arr = find_k_max_number_in_an_array(nums2, p)
            
            # merge two array with everytime taking lexicographily larger list
            # https://leetcode.com/problems/create-maximum-number/discuss/77286/Short-Python-Ruby-C%2B%2B
            # see explanation
            curr_arr = merge_two_array(first_arr, second_arr)
            #print(curr_arr)
            
            # can be directly use python max function
            if compare_two_array(curr_arr, ans):
                ans = curr_arr
            # ans = max(ans, curr_arr) if ans else curr_arr
            
            #print(ans)
        
        return ans
