class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        # Step-1: Convert Binary To Decimal
        
        def func(x):
            s = 0
            x = x[::-1]
            for i in range(len(x)):
                z = pow(2,i)*int(x[i])
                s = s + z
            return s
        
    
        m = func(a)
        n = func(b)
        
        # Step-2: Sum of Both Decimal
        Sum = m+n
        
        # Step-3: Converting The Sum  Into The Binary
        
        SStr = ""
        if(Sum==0):
            return "0"
        while(Sum>0):
            rem = Sum%2
            Sum = Sum//2
            SStr = SStr + str(rem)
        SStr = SStr[::-1]
        return SStr
