class Solution:
	def isPalindrome(self, head: Optional[ListNode]) -> bool:
		values = []
		while head: 
			values.append(head.val)
			head = head.next

		n = len(values)
		for i in range(n//2):
			if not values[i] == values[-(i+1)]: return False
		return True
