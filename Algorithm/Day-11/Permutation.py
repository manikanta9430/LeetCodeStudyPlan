class Solution:
    bigger=[]
    def helper(self, nums, build):
        if len(nums)==0: self.bigger.append(build)
        for i in range(len(nums)):
            self.helper(nums[0:i]+nums[i+1:],build+[nums[i]])
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.bigger=[]
        self.helper(nums,[])
        return self.bigger
