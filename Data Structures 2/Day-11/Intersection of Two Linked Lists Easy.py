class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        a_len = 0
        b_len = 0
        
        a_node = headA
        while a_node:
            a_len+=1
            a_node = a_node.next
        
        b_node = headB
        while b_node:
            b_len+=1
            b_node = b_node.next
        
        diff=abs(b_len-a_len)
        if a_len >= b_len:
            lar = headA
            sm = headB
        else:
            lar = headB
            sm = headA
        
        for i in range(diff):
            lar = lar.next
        
        while lar and sm:
            if lar == sm:
                return lar
            lar = lar.next
            sm = sm.next
        return None
