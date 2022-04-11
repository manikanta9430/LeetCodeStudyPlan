class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(0,head)
        prev = dummy
        curr = head.next
        while curr:
            flag = False
            while curr and curr.val == prev.next.val:
                curr = curr.next
                flag = True
            if flag:
                prev.next = curr
                if curr == None:
                    break
                curr = curr.next
            else:
                prev = prev.next
                if curr == None:
                    break
                curr = curr.next
                
        return dummy.next
