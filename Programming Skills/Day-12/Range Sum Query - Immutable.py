class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums        

    def sumRange(self, left: int, right: int) -> int:
        self.left = left
        self.right = right
        return sum(self.nums[left:right+1])    
