class Solution:
	def largestRectangleArea(self, heights: List[int]) -> int:
		# Pre-routine to check if the array is sorted or if it only has one unique value

		n , last = len(heights), heights[0]
		min_ , max_ = inf , -inf
		increase, decrease = 0, 0
		for h in heights:
			increase += (h >= last)
			decrease += (h <= last)
			max_ = max(max_,h)
			min_ = min(min_,h)
			last = h 

		if min_ == max_: return min_*len(heights)

		def DivConc(start, end, current_max):
			if not start <= end: return 0
			if increase == n:
				smallest = heights[start]
				idx = start
			elif decrease == n:
				smallest = heights[end]
				idx = end
			else:
				smallest = heights[start]
				idx = start
				for i in range(start,end+1):
					if smallest > heights[i]:
						smallest = heights[i]
						idx = i

			current_max = max(current_max, (end-start+1)*smallest)
			left = DivConc(start,idx-1, current_max)
			right = DivConc(idx+1,end,current_max)
			return max(current_max, left, right)

		return DivConc(0,len(heights)-1,0)
