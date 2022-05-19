class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        l=len(nums)
        ans=[0]*l
        arr=[nums[-1]]
        
        i=l-2
        
        for n in nums[-2::-1]:#Starting from 2nd last el
            lo,hi=0,len(arr)-1
            while lo<=hi:
                mid=lo+(hi-lo)//2
                if arr[mid]>n:
                    hi=mid-1
                else:
                    lo=mid+1
            arr.insert(lo,n)
            j=lo-1
            while j>=0 and arr[j]==n:#In case num is duplicate like [-1,-1]
                j-=1
            ans[i]=j+1
            i-=1
        return ans
