class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        max_solutions = 1<<n
        # for duplicated list, 
        # we must sort the array before counting, to avoid duplication in result
        nums = sorted(nums)
        for i in range(max_solutions):
            bin_i = bin(i)[2:].zfill(n)
            round_res = [nums[idx] for idx, c in enumerate(bin_i) if c == "1"]
            # list can not be added into set, but tuple can!!!!!!!!!
            res.add(tuple(round_res))
        return res
