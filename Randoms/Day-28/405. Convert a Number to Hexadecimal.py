class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'

        hex_dict = {
            10:'a',
            11:'b',
            12:'c',
            13:'d',
            14:'e',
            15:'f'
        }
        
        if num < 0:
            num = 4294967296 + num
            
            
        hex_num = ''

        while num > 0:
            remain = num % 16
            if remain < 10:
                hex_num = str(remain) + hex_num
            else:
                hex_num = hex_dict[remain] + hex_num
            num //=16
                
        return hex_num
