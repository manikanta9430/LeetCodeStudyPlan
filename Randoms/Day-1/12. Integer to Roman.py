class Solution(object):
    def intToRoman(self, num):
	
        roman = ''
        
        while num % 1000 != num:
            roman += 'M'
            num -= 1000
            
        while num % 500 != num:
            roman += 'D'
            num -= 500
        
        while num % 100 != num:
            roman += 'C'
            num -= 100
        
        while num % 50 != num:
            roman += 'L'
            num -= 50
        
        while num % 10 != num:
            roman += 'X'
            num -= 10
        
        while num % 5 != num:
            roman += 'V'
            num -= 5
        
        while num != 0:
            roman += 'I'
            num -= 1
            
            
        #fix edge cases
        roman = roman.replace('DCCCC', 'CM')
        roman = roman.replace('LXXXX', 'XC')
        roman = roman.replace('IIII', 'IV')
        roman = roman.replace('VIV', 'IX')
        roman = roman.replace('XXXX', 'XL')
        roman = roman.replace('CCCC', 'CD')
        
        return roman
