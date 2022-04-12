class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        return deepcopy(head)
