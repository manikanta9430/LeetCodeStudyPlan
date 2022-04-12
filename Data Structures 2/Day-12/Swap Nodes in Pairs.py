class Solution:
	def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
		if not head: return head
		root = head.next if head.next else head
		last = ListNode(0,head.next)
		while head and head.next:
			last.next = head.next
			temp = head.next.next
			head.next.next = head
			head.next = temp

			last = head
			head = head.next


		return root
