class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.combinationSum2_sorted(candidates, target)
        
    def combinationSum2_sorted(self, candidates, target):
        res=[]
        if target in candidates:
            res.append([target])
        
        for i in range(len(candidates)):
            v = candidates[i]
            if v > target//2:
                break
            elif i==0 or candidates[i]!=candidates[i-1]:
                res_next = self.combinationSum2_sorted(candidates[(i+1):], target-v)
                for res1 in res_next:
                    res.append([v] + res1)
                    
        return res
