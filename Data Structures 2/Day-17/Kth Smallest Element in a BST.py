import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        min_heap = []
        stack = [root]
        
        while stack:
            curr = stack.pop()
            heapq.heappush(min_heap, curr.val)
            
            if curr.left:
                stack.append(curr.left)
                
            if curr.right:
                stack.append(curr.right)
                
        while k > 1:
            heapq.heappop(min_heap)
            k -= 1
            
        return min_heap[0]
