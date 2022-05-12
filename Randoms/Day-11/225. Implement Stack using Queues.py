class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyStack:

    def __init__(self):
        self.stack = None
        self.size = 0
        self.current = self.stack

    def push(self, x: int) -> None:
        self.size += 1
        if not self.stack:
            self.stack = Node(x)
            self.current = self.stack
        else:
            new_node = Node(x)
            new_node.prev = self.current
            self.current.next = new_node
            self.current = self.current.next

    def pop(self) -> int:
        if not self.empty():
            self.size -= 1
            if self.current and not self.current.prev:
                val = self.current.val
                self.stack = None
                self.current = None
                return val
            pop = self.current.val
            self.current = self.current.prev
            self.current.next = None
            return pop
            
    def top(self) -> int:
        if not self.stack:
            return -1
        return self.current.val

    def empty(self) -> bool:
        if self.size == 0:
            return True
        return False
