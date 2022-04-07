class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def check(l):
            k=l[1]-l[0]
            for i in range(2,len(l)):
                if l[i] != l[i-1] + k:
                    return False 
            return True
        ans=[]
        for i in range(len(r)):
            ans.append(check(sorted(nums[l[i]:r[i]+1])))
        return ans
