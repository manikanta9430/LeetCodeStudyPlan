class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bs(l,r,arr,tar):
            while l<=r:
                mid=(l+r)//2
                if arr[mid]==tar:
                    return True
                elif arr[mid]>tar:
                    r=mid-1
                else:
                    l=mid+1 
            return False
        
        for i in range(len(matrix)):
            if bs(0,len(matrix[0])-1,matrix[i],target):
                return True 
        return False
