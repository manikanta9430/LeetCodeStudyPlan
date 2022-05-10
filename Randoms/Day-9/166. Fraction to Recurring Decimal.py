class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        
        if numerator % denominator == 0:
            return str(numerator // denominator)
        
        negative = "-" if numerator * denominator < 0 else ""
        
        if numerator > 0:
            numerator = -numerator
        if denominator > 0:
            denominator = -denominator
        
        quotient = numerator // denominator
        
        remaining = numerator % denominator
        
        ans = negative + str(quotient) + "."
        decimal = []
        
        seen = {remaining: 0}
        
        while remaining:
            numerator = remaining * 10
            
            quotient = numerator // denominator
            decimal.append(str(quotient))
            
            remaining = numerator % denominator
            if remaining in seen:
                break
                
            seen[remaining] = len(decimal)
            
        if remaining == 0:
            return ans + "".join(decimal)
        
        for i, d in enumerate(decimal):
            if (i == seen[remaining]):
                ans += "("
            ans += d
        ans += ")"
        
        return ans
