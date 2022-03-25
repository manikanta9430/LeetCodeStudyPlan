class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def dfs(n):
            if not n or not n.left: return

            n.left.next = n.right
            if n.next: n.right.next = n.next.left
            dfs(n.left)
            dfs(n.right)

        dfs(root)
        return root
