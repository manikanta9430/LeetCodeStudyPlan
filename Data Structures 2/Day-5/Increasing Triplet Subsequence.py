class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        stack = []
        for num in nums:
            if not stack:
                stack.append(num)
            # This is a classic way to keep the stack longest.
            else:
                if stack and stack[-1] >= num:
                    i = bisect.bisect_left(stack, num) 
                    stack[i] = num
                else:
                    stack.append(num)
        return len(stack) >= 3
