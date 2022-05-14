class Solution:
	def arrangeCoins(self, n: int) -> int:
		sqrt_n = int((2*n)**(0.5))
		res = None
		for j in range(sqrt_n-1, sqrt_n+2):
			if (j-1)*j<2*n<=j*(j+1):
				if 2*n==j*(j+1):
					res = j
				else:
					res = j-1
				break
		return res 
