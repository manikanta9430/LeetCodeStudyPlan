class Solution:
    def lengthOfLIS(self, nums):
        top = [(-float('inf'), 0)]
        for n in nums:
            top_count = max(filter(lambda x: x[0] < n, top), key=lambda x: x[1])[1]
            top.append((n, top_count + 1))
        
        return max(top, key=lambda x: x[1])[1]
