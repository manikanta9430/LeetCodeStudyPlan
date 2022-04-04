class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        
        if not T:
            return []
        
        res = [0] * len(T)
        
		# decreasing stack
        stack = []
        
        for i in range(len(T)):
            
            while stack and T[i] > T[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx
            
            stack.append(i)
        
        return res
