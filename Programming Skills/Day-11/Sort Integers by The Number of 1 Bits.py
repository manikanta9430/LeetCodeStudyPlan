class Solution(object):
    def sortByBits(self, arr):
    
        temp = []
        res = []
        
        for i in range(len(arr)):
            temp.append((bin(arr[i]).count('1'), arr[i]))
        
        temp = sorted(temp)
        
        for i in range(len(temp)):
            res.append(temp[i][1])
            
        return res
