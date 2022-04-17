class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.val = 0
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, index: int) -> int:
        dummyhead = self.head
        while index+1:
            dummyhead = dummyhead.next
            index -= 1
        if not (dummyhead is None or dummyhead.next is None):
            return dummyhead.val
        return -1

    def addAtHead(self, val: int) -> None:
        dummyhead = self.head
        NewNode = ListNode(val)
        nextNode =  dummyhead.next 
        dummyhead.next = NewNode
        NewNode.next = nextNode
        nextNode.prev = NewNode
        NewNode.prev = dummyhead
        
    def addAtTail(self, val: int) -> None:
        dummytail = self.tail
        NewNode = ListNode(val)
        pre = self.tail.prev
        self.tail.prev = NewNode
        NewNode.prev = pre
        pre.next = NewNode
        NewNode.next = self.tail

    def addAtIndex(self, index: int, val: int) -> None:
        dummyhead = self.head
        while index+1:
            dummyhead = dummyhead.next
            index -= 1
        if not (dummyhead is None):       
            NewNode = ListNode(val)
            pre = dummyhead.prev
            nex = dummyhead
            dummyhead.prev.next = NewNode
            dummyhead.prev = NewNode
            NewNode.next = nex
            NewNode.prev = pre
        
    def deleteAtIndex(self, index: int) -> None:
        dummyhead = self.head
        while index+1:
            dummyhead = dummyhead.next
            index -= 1
        if not (dummyhead is None or dummyhead.next is None):
            pre = dummyhead.prev
            nex = dummyhead.next
            dummyhead.prev.next = nex
            dummyhead.next.prev = pre
            dummyhead.next = None
            dummyhead.prev = None
