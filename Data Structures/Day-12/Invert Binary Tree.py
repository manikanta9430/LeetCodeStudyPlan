class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        from queue import Queue
        if root == None:
            return None
        queue = Queue()
        queue.put(root)
        while not queue.empty():
            curr_root = queue.get()
            temp = curr_root.left
            curr_root.left = curr_root.right
            curr_root.right = temp
            if curr_root.left:
                queue.put(curr_root.left)
            if curr_root.right:
                queue.put(curr_root.right)
        return root
