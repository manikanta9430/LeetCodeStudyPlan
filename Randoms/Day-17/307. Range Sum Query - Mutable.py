class BinaryIndexedTree:

	def __init__(self, num_items):
		self.sums = [0 for i in range(1+num_items)]
		self.sums_len = len(self.sums)

	def update(self, i, delta):
		while i<self.sums_len: 
			self.sums[i] += delta
			i += i&(-i)

	def query(self, i):
		res = 0
		while i>0: 
			res += self.sums[i]
			i -= i&(-i)
		return res    


class NumArray:

	def __init__(self, nums: List[int]):
		self.nums = nums
		self.nums_len = len(self.nums)
		self.binary_indexed_tree = BinaryIndexedTree(self.nums_len)
		for i in range(self.nums_len):
			self.binary_indexed_tree.update(i+1, self.nums[i])

	def update(self, index: int, val: int) -> None:
		delta = val - self.nums[index]
		self.binary_indexed_tree.update(index+1, delta)
		self.nums[index] = val

	def sumRange(self, left: int, right: int) -> int:
		return self.binary_indexed_tree.query(right+1) - self.binary_indexed_tree.query(left)
