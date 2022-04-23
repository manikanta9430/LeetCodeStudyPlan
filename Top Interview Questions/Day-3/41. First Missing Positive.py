class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set(nums)
		# Ans range := [1...l+1]
		ans = len(nums) + 1  # Worst Case (No Mising)
		for i in range(1, ans):
			if i not in s:
				return i
		return ans
