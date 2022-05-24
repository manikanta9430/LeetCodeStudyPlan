class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
                
        def solve(arr,n):
            st=0
            ed=len(arr)-1
            while st<=ed:
                mid=(st+ed)//2
                if arr[mid]==n:
                    return mid
                elif arr[mid]>n:
                    ed=mid-1
                else:
                    st=mid+1
            return st
        
        
        n = len(envelopes)
        if n <= 1:
            return n
        envelopes = sorted(envelopes, key=lambda x:(x[1], -x[0]))
        ans = [envelopes[0][0]]
        
        for i in range(1, n):
            num = envelopes[i][0]
            if ans[-1] < num:
                ans.append(num)
            elif ans[-1] > num:
                # use binary search 
                idx = solve(ans, num)
                ans[idx] = num
        
        return len(ans)
