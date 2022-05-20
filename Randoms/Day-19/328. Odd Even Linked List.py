class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # O(N), O(N) -> easy
         
        # O(N), O(1)
        return self.sol2(head)
    
    # single pointer
    def sol1(self, head):
        if not head or not head.next: return head

        odd_head = head
        even_head = head.next
            
        pre, curr, nxt = head, head.next, None
        flag = False
        
        while curr.next:
            nxt = curr.next
            pre.next = nxt
            pre = curr
            curr = nxt
            flag = not flag
            
        if flag:
            pre.next = None
            curr.next = even_head
        else:
            pre.next = even_head

        return odd_head

    
    # double pointer
    def sol2(self, head):
        if not head: return head
        
        even_head = head.next
        odd, even = head, even_head
        
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        
        odd.next = even_head
        return head
