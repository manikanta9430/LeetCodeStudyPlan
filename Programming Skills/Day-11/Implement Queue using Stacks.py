class MyQueue:

    def __init__(self):
        self.instack = []
        self.outstack = []

    def push(self, x: int) -> None:
        if self.outstack == []:
            self.instack.append(x)
        else:
            while self.outstack != []:
                self.instack.append(self.outstack.pop())
            self.instack.append(x)

    def pop(self) -> int:
        while self.instack != []:
            self.outstack.append(self.instack.pop())
        return self.outstack.pop()

    def peek(self) -> int:
        if self.outstack == []:
            return self.instack[0]
        elif self.instack == []:
            return self.outstack[-1]

    def empty(self) -> bool:
        return self.instack == [] and self.outstack == []
