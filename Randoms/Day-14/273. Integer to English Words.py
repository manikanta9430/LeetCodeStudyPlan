import math

class Solution:
    num_map = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
        100: 'hundred',
        1000: 'thousand',
        1000000: 'million',
        1000000000: 'billion'
    }
    
    def numberToWords(self, num: int) -> str:
        return ' '.join([s.capitalize() for s in self.split_num(num)])

    def split_num(self, num: int) -> str:
        ret = []
        q = rem = 0
        if num == 0:
            return ['zero']
        for n in sorted(self.num_map.keys(), reverse=True):
            if n > num:
                continue
            q, rem = divmod(num, n)
            if q > 19:
                ret.extend(self.split_num(q))
            elif num >= 100:
                ret.append(self.num_map[q])
            ret.append(self.num_map[n])

            if rem > 19:
                ret.extend(self.split_num(rem))
            elif rem:
                ret.append(self.num_map[rem])
            break

        return ret
