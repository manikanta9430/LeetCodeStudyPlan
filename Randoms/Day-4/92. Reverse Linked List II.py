class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        #edge case 1
        if left == right:
            return head
        
        nodesToReverse = right - left
        
        #traverse till left position 
        prev, curr = None, head
        i = 1
        while i < left and curr:
            prev, curr = curr, curr.next
            i += 1
        
        i = 0
        tempPrev = prev
        prev, curr = curr, curr.next
        
        #edge case 
        if not tempPrev: 
            tempPrev = prev
        
        while i < nodesToReverse and curr:
            i += 1
            nxt = curr.next
            
            #reverse list
            curr.next = prev
            prev = curr
            curr = nxt
        
        #adjust start and end pointers 
        if left > 1:
            leftNode = tempPrev.next
            leftNode.next = nxt
            tempPrev.next = prev
        else:
            tempPrev.next = curr
        
        return head if left > 1 else prev
