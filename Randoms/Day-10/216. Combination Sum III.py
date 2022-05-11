import itertools
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        return [list(item) for item in itertools.combinations(range(1,10),k) if sum(item) == n] 
