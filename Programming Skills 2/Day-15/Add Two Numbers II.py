class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x=""
        y=""
        while l1:
            x+=str(l1.val)
            l1=l1.next
        while l2:
            y+=str(l2.val)
            l2=l2.next
        z=int(x)+int(y)
        dum=pre=ListNode(0)
        for i in str(z):
            dum.next=ListNode(int(i))
            dum=dum.next
        return pre.next
