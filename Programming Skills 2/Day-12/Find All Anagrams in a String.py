class Solution:
	def findAnagrams(self, s: str, p: str) -> List[int]:
		d = dict()
		words = "abcdefghijklmnopqrstuvwxyz"
		for i,j in enumerate(words):
			d[j] = i + 1
		l1 = [0] * 27 # For storing the count of letters in string p.
		for i in p:
			val = d[i]
			l1[val] += 1
		k = len(p)
		n_s = len(s)

		l2 = [0] * 27 # This would act as a intermeddaite list for string s.
		c = 0 # count variable.
		res = list() # resultant list.
		for i in range(n_s):
			c += 1
			v = d[s[i]]
			l2[v] += 1
			if c==k:     # when count is equal to length of string p.
				val = i + 1 - k
				if l1 == l2:
					res.append(val)
				l2[d[s[val]]] -= 1  # d[s[val]]->would bring the value at which the letter is present in l2.
				c -= 1
		return res
