class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        
        def to_int(digits):
            value = 0
            for digit in digits:
                value = (value << 1) + digit
            
            return value
        
        def clock(digits):
            
            hours = to_int(digits[0:4])
            minutes = to_int(digits[4:])
        
            if hours > 11 or minutes > 59:
                return ""
        
            return f"{hours}:{minutes:02d}"
        
        def permut_digits(n, count = 0, digits = []):
            #if n - len(digits) < n - count:
            #    return []
            
            if len(digits) == 10:
                result = []
                if count == n:
                    s = clock(digits)
                    if s:
                        result.append(s)
                return result
            
            result = []
            for digit in [0, 1]:
                digits.append(digit)
                result.extend(permut_digits(n, count + digit, digits))
                digits.pop()


            return result
        
        return permut_digits(turnedOn)
