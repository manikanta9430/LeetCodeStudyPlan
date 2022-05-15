class Solution:
    def addDigits(self, num: int) -> int:
        if(num<10):
            return num
        nums=0
        while(num>0):
            nums+=num%10
            num=num//10            
            
        return self.addDigits(nums)
