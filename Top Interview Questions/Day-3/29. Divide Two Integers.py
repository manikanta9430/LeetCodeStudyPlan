class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX, MIN = 2147483647, -2147483648
        quo, remainder, d = 0, abs(dividend),  abs(divisor)
        negative = (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0)

        while remainder >= d:
            mul, total = self.power_up(remainder, d)
            quo += mul
            remainder -= total
			
        return max(MIN, -quo)  if negative else min(MAX, quo)
    
    def power_up(self, remainder, d):
        multiplier = 1
        while remainder >= d + d:
            d += d
            multiplier += multiplier
            
        return multiplier, d
