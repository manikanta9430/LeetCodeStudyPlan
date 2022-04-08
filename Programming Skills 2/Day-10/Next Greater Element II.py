class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack=[[0,nums[0]]]
        n=len(nums)
        ans=[-1 for _ in range(n)]
        i=1
        while i<2*n-1:
            while stack and stack[-1][1]<nums[i%n]:
                k=stack.pop()
                ans[k[0]]=nums[i%n]
            stack.append([i%n,nums[i%n]])
            i+=1
        return ans
