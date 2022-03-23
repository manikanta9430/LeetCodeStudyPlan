class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res =0
        n=len(arr)
        for i in range(n):
            for j in range(i,n,2):
                res += sum(arr[i:j+1])
        return res
