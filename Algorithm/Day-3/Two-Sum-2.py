#BruteForce Method(My Solution), This method is working efficiently for Smaller Arrays but for bigger ones, we get MTL error.
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if((numbers[i]+numbers[j])==target):
                    return [i+1,j+1]
        
#So to solve this issue, we can use alternate method called "Two-pointer"
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        while l<r:
            if numbers[l]+numbers[r]==target:
                return [l+1,r+1]
            if numbers[l]+numbers[r]> target:
                r -=1
            if numbers[l]+numbers[r] < target:
                l +=1
        
