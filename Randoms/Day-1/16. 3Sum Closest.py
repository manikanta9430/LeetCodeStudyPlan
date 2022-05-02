class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        scope = len(nums)
        closest = float('inf')
        output = 0
        for i in range(scope-2):
            low = i+1
            high = scope-1
            while low < high:
                total = nums[low]+nums[high]+nums[i]
                distance = abs(total - target)
                if distance < closest:
                    closest = distance
                    output = total
                if total < target:
                    low += 1
                else:
                    high -=1       
        return output
