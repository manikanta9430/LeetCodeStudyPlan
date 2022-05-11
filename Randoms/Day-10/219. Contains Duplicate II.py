from collections import Counter

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l=[]
       
        coun = Counter(nums)
        for i in coun:
            if coun[i] >= 2:
                l.append(i)
                
        for j in range(len(l)):
            index=[]
            for i in range(len(nums)):
                if nums[i] == l[j]:
                    index.append(i)
                    
            for s in range(len(index)):
                diff =0
                for m in range(s+1,len(index)):
                    diff=abs(index[s]-index[m])
                    if diff <=k:
                        return True
                
        return False  
