class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i=1 #the 0-th index num will always unique
        j=1
        n=len(nums)
        
        while j<n:
            
            if nums[j]!=nums[j-1]: #break point, encounter a new number so just put that in order
                nums[i]=nums[j]  #just replace the duplicate with other number
                i+=1
                
            j+=1
            
        return i
