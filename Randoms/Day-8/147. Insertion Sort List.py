class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:   
        dummy = ListNode(0, head)
        prevI, i = dummy, head

        while i:
            prevJ, j = dummy, dummy.next
            while j.val < i.val:
                prevJ, j = j, j.next

            if i is j:
                prevI, i = i, i.next
            else:
                prevI.next = i.next
                i.next = j
                prevJ.next = i
                i = prevI.next
  
        return dummy.next
