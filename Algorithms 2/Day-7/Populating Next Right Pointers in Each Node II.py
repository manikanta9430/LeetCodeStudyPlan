class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        def walkBT(node, level, node_lst):
            if len(node_lst) < level + 1:
                node_lst.append([])
                
            node_lst[level].append(node)
            
            if node.left:
                walkBT(node.left, level+1, node_lst)
            if node.right:
                walkBT(node.right, level+1, node_lst)
                
        node_lst = []
        walkBT(root, 0, node_lst)
        
        for level in range(len(node_lst)):
            for i in range(1, len(node_lst[level])):
                node_lst[level][i-1].next = node_lst[level][i]
            
        return root
