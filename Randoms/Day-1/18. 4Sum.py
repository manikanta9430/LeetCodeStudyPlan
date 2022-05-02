class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        nums.sort()
        res_temp = []
        for i in range(0, len(nums) - 3):
            if i == 0 or nums[i] != nums[i-1]:
                for j in range(i + 1, len(nums)):
                    if (j == i+1) or (nums[j] != nums[j-1]):
                        cur_target = target - nums[i] - nums[j]
                        comb = self.twoSum(j+1, len(nums)-1, nums, cur_target, nums[i], nums[j])
                        res_temp += comb
        return res_temp
                   
            
    def twoSum(self, left, right, nums, target, frist, second):
        res_temp = []
        while left < right:
            if (nums[left] + nums[right]) == target:
                res_temp.append([nums[left], nums[right], frist, second])
                left += 1
                right -= 1
                while nums[left] == nums[left-1] and left < right:
                    left += 1
            elif (nums[left] + nums[right]) > target:
                right -= 1
            elif (nums[left] + nums[right]) < target:
                left += 1
        return res_tem
