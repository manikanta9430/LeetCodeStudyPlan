class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        up_or_down = 0                          # 1 means last_number  > current_number, -1 means 1 means last_number  > current_number
        count_of_removed_number = 0
        
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                if up_or_down == 1:             # since we were excepting -1 but we got 1, so we will remove one number
                    count_of_removed_number += 1
                up_or_down = 1
            elif nums[i-1] < nums[i]:
                if up_or_down == -1:            # since we were excepting 1 but we got -1, so we will remove one number
                    count_of_removed_number += 1
                up_or_down = -1
            else:
                count_of_removed_number += 1    # since last number is equal to current number, so one of number will be removed
        
        return len(nums) - count_of_removed_number
