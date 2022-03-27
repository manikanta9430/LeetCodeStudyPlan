class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = head
        while tmp and tmp.next:
            head = head.next
            tmp = tmp.next.next
        return head
