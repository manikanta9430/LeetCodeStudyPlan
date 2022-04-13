class Solution:
    
    def reverseList(self, head : Optional[ListNode]) -> Optional[ListNode]:
        prev_node = None
        cur_node = head
        
        while cur_node:
            next_node = cur_node.next
            cur_node.next = prev_node
            
            prev_node = cur_node
            cur_node = next_node
        
        return prev_node
    
    def insert_after(self, list_node, node):
        node.next = list_node.next
        list_node.next = node
        
        
    def delete_head(self, head: Optional[ListNode]):
        
        if not head:
            return None,None
        
        node = head
        head = head.next
        
        return head, node
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        fast_runner = slow_runner = head
        
        while fast_runner and fast_runner.next:
            fast_runner = fast_runner.next.next
            slow_runner = slow_runner.next
        
        # After above while loop, we have slow runner in the middle
        # Reverse the list from slow_runner
        
        slow_runner = self.reverseList(slow_runner)
        
        l1_head = head
        l2_head = slow_runner
        
        while l2_head:
            l2_head, l2_node = self.delete_head(l2_head)
            self.insert_after(l1_head, l2_node)
            l1_head = l1_head.next.next
            
        l1_head.next = None
            
        return
