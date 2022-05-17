class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def dfs(prev1, prev2, rem):
            if not rem:
                return True
            
            for i in range(1, len(rem)+1):
                if rem[:i].startswith('0') and len(rem[:i]) > 1:
                    return False
                if prev1 + prev2 == int(rem[:i]):
                    if dfs(prev2, int(rem[:i]), rem[i:]):
                        return True
            
            return False
        
        for i in range(2, len(num)):
            for j in range(1, i):
                if num[:j].startswith('0') and len(num[:j]) > 1:
                    continue
                if num[j:i].startswith('0') and len(num[j:i]) > 1:
                    continue
                if dfs(int(num[:j]), int(num[j:i]), num[i:]):
                    return True
        
        return False
