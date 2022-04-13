class Solution:
    def reverseN(self, head, k):
        prev = None
        node = head
        _next = None
        for _ in range(k):
            _next = node.next
            node.next = prev
            prev = node
            node = _next
        return prev, head
            
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1: return head
        l, r = ListNode(next=head), head
        d = l
        while r:
            idx = 0
            while idx < k and r:
                idx += 1
                r = r.next
            if idx != k: break
            l.next, l = self.reverseN(l.next, k)
            l.next = r
        return d.next
