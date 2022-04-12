class Solution:
	def canJump(self, nums: List[int]) -> bool:
		from heapq import heappush, heappop, heapify
		visited = []
		min_index = 0
		for i in range(len(nums)):
			while min_index < i:
				if len(visited) == 0:
					return False
				min_index = heappop(visited)
			heappush(visited, nums[i] + i)
		return True
