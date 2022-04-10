class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res=[]
        
        def BT(ind,target,path):
            if target==0:
                res.append(path)
                return
            if ind==-1:
                return
            if target<0:
                return 
            BT(ind-1,target,path)   #Not take
            BT(ind,target-nums[ind],path+[nums[ind]])  
        
        BT(len(nums)-1,target,[])
        return res
