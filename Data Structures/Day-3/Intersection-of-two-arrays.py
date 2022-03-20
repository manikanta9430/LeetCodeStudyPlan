class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = []
        d1,d2={},{}
        
        for i in nums1:
            if i not in d1:
                d1[i]=1
            else:
                d1[i]+=1
        for j in nums2:
            if j not in d2:
                d2[j]=1
            else:
                d2[j]+=1
        for k in d1:
            if k in d2:
                for x in range(min(d1[k],d2[k])):
                    arr.append(k)
        return arr
