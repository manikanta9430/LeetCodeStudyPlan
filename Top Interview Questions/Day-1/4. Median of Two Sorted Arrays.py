class Solution:
	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

		n, m = len(nums1), len(nums2)

		nums = [0]*(m+n)
		p, p1, p2 = 0 , 0, 0

		while p < m+n:
			if not p1 < n: 
				nums[p] = nums2[p2]
				p2 += 1
			elif not p2 < m:
				nums[p] = nums1[p1]
				p1 += 1

			elif nums1[p1]<nums2[p2]:
				nums[p] = nums1[p1]
				p1 += 1
			else:
				nums[p] = nums2[p2]
				p2 += 1
			p += 1

		if (m+n)%2 == 0: return (nums[(m+n)//2]+nums[(m+n)//2-1])/2
		else: return nums[(m+n)//2]
