class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(',')
        stack = [None]
        for i, node in enumerate(nodes):
            if node != '#':
                stack.append(node)
            else:
                if len(stack) <= 1 and i != len(nodes) - 1:
                    return False
                node = stack.pop()
        return len(stack) == 0
