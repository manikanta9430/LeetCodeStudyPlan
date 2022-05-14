class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        for i in range(n-1, 0,-1):
            low = 0
            high = i-1
            while low < high:
                if nums[low]+nums[high] > nums[i]:
                    count += high - low
                    high -= 1
                else:
                    low += 1
        return count
