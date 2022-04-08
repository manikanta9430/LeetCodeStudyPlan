class Solution:
    def nextGreaterElement(self, n: int) -> int:
        
        # getting each digit - [1, 2, 3]
        nums = list(map(int, str(n)))
        
        # check if descending order
        idx = len(nums) - 2 # 2nd last el
        while idx >= 0 and nums[idx] >= nums[idx + 1]:
            idx -= 1
            
        if idx < 0:
            return -1
        
        # idx of num after idx which is less than idx's value
        idx2 = len(nums) - 1 # last el
        while nums[idx2] <= nums[idx]:
            idx2 -= 1
            
        # swap and reverse
        nums[idx], nums[idx2] = nums[idx2], nums[idx]
        nums[idx + 1:] = reversed(nums[idx + 1:])
        
        # return res
        res = ''
        for n in nums:
            res += str(n)
            
        res = int(res)
        return res if res <= 2**31 - 1 else -1 # inbound 32-bit int - 2147483647

