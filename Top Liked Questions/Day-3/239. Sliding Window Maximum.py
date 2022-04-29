class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack=list();ans=list()
        for i in range(k):
            while len(stack) and stack[-1][-1]<=nums[i]:
                stack.pop()
            stack.append([i,nums[i]])
        ans.append(stack[0][1])
        start=0
        for i in range(k,len(nums)):
            while len(stack) and stack[-1][-1]<=nums[i]:
                stack.pop()
            if len(stack) and stack[0][0]==start:stack.pop(0)
            stack.append([i,nums[i]])
            ans.append(stack[0][1])
            start+=1
        return ans
