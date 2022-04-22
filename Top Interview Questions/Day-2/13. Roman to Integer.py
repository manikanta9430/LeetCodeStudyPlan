class Solution:
    def romanToInt(self, s: str) -> int:
        
        can_be_before = {"I":{"V","X"}, "X":{"L","C"}, "C":{"D","M"}}
        symbol_value = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        
        symbol_length = len(s)
        total_val = 0
        to_minus = 0
        for index, val in enumerate(s):
            sv = symbol_value.get(val)
            
            #print(f"index = {index}, val={val}, sv={sv}, total_val={total_val}, to_minus={to_minus}")
            if (index < symbol_length - 1) and (s[index + 1] in can_be_before.get(val, {})):
                to_minus = sv
            else:
                total_val += (sv - to_minus)
                to_minus = 0
                
        return total_val
