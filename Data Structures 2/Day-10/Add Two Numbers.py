class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1=""
        s2=""
        while l1:
            s1+=str(l1.val)
            l1=l1.next
        while l2:
            s2+=str(l2.val)
            l2=l2.next
        i=0
        s3=str(int(s1[::-1])+int(s2[::-1]))
        s3=[int(n) for n in s3]
        s3=s3[::-1]
        anshead=ListNode()
        i=0
        ans=anshead
        for s in s3:
            ans.val=int(s)
            if i!=len(s3)-1:
                ans.next=ListNode()
                ans=ans.next
            else:
                ans.next=None
            i+=1
        return anshead
