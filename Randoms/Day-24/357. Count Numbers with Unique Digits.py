class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        d = 0 
        i = 1 
        while i<=n:
            b = 9
            c = i-1
            x = 9
            while c>0:
                x*=b
                b-=1
                c-=1
            d+=x
            i+=1
        return d+1
