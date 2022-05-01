class Solution(object):
    def findTargetSumWays(self, nums, target):
        memo={}
        
        def temp(curr,su):
            if((curr,su) in memo):
                return memo.get((curr,su))
            if(curr==len(nums)):
                if(su==target):
                    return 1;
                else:
                    return 0;
            c1=temp(curr+1,su+nums[curr]);
            c2=temp(curr+1,su-nums[curr]);
            memo[(curr,su)]=c1+c2
            return c1+c2
        return temp(0,0);
