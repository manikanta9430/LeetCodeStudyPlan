class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        arr = list()
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
            
        def getBst(arr):
            if not arr:
                return None
            mid = len(arr)//2
            node = TreeNode(arr[mid])
            node.left = getBst(arr[:mid])
            node.right = getBst(arr[mid+1:])
            return node
        
        return getBst(arr)
