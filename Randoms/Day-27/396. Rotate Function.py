class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        F = [0]*len(nums)
        n = len(nums)
        F[0] =sum([i*nums[i] for i in range(n)]) #can be initialized using the function
        sum_nums = sum(nums)
        for i in range(n-1):
            F[i+1] = F[i] - n * nums[-1-i] +sum_nums
        return max(F)
