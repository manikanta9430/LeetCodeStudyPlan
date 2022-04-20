class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = nums
        self.return_arr = []
        print(nums)

    def reset(self) -> List[int]:
        self.nums = self.original
        return self.nums
        

    def shuffle(self) -> List[int]:
        self.return_arr = []
        rad_samp = random.sample(range(0, len(self.nums)), len(self.nums))
        for indecie in rad_samp:
            self.return_arr.append(self.nums[indecie])
        return self.return_arr
