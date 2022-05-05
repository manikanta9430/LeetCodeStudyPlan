class Solution:
    def partition1(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head
        
        smaller = ListNode(0,None)
        start = smaller
        last = None
        bigger = ListNode(0,None)
        first = bigger
        h = head
        while h:
            if h.val < x:
                smaller.next = ListNode(h.val,None)
                smaller = smaller.next
                last  = smaller
            else:
                bigger.next = ListNode(h.val,None)
                bigger = bigger.next 
            h = h.next
        if last:
            last.next = first.next
            return start.next
        else:
            return first.next
        
        
        def partition2(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        size_dict = {"smaller":[], "bigger":[]}
        h = head
        while h:
            location = "smaller" if h.val < x else "bigger"
            size_dict[location] = size_dict.get(location,[]) + [h.val]
            h = h.next
        smaller,last = self.ls_from_list(size_dict["smaller"])
        bigger,_ = self.ls_from_list(size_dict["bigger"])
        print(last)
        if last:
            last.next = bigger
            return smaller
        else:
            return bigger

   
    def ls_from_list(self, lst : list[int])-> ListNode:
        ans = ListNode(0,None)
        last = None
        temp = ans
        for num in lst:
            temp.next = ListNode(num,None)
            temp = temp.next
            last = temp
        return ans.next,last
