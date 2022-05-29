class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        jumplist = {stone:set() for stone in stones}
        jumplist[1].add(1)
        
        for stone in jumplist:
            for prev_jump in jumplist[stone]:
                for jump in (prev_jump-1, prev_jump, prev_jump+1):
                    if jump > 0 and stone+jump in jumplist:
                        jumplist[stone+jump].add(jump)
        return len(jumplist[stones[-1]]) > 0
