class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.inOrderBST = []
        def getInorder(node):
            if not node:
                return
            getInorder(node.left)
            self.inOrderBST.append(node.val)
            getInorder(node.right)
        getInorder(root)
        self.ptr = -1
        self.len = len(self.inOrderBST)

    def next(self) -> int:
        self.ptr += 1
        return self.inOrderBST[self.ptr]

    def hasNext(self) -> bool:
        if self.ptr < self.len - 1:
            return True
