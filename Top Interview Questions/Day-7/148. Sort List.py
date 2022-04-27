class Solution(object):
    def sortList(self, head):
        arr=[]
        dup=head
        while dup:
            arr.append(dup.val)
            dup=dup.next
        arr.sort()
        a=head
        for i in arr:
            a.val=i
            a=a.next
        return head
