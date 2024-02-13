class MyLinkedList:

    def __init__(self):
        self.dummy = Node()

    def get(self, index: int) -> int:
        i = 0 
        curr = self.dummy.next
        # print(self.dummy)
        
        while curr and i < index:
            curr = curr.next
            i += 1
        if curr:
            return curr.value
        else:
            return -1


    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        # print(self.dummy)
    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        curr = self.dummy
        while curr.next != None:
            curr = curr.next
        curr.next = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = Node(val)
        curr = self.dummy
        i = 0
        while curr and i < index:
            curr = curr.next
            i += 1
        if curr:
            new_node.next = curr.next
            curr.next = new_node


    def deleteAtIndex(self, index: int) -> None:
        curr = self.dummy
        i = 0
        while curr and i< index:
            curr = curr.next
            i += 1
        if curr and curr.next:
            curr.next = curr.next.next

class Node:
    def __init__(self,value=0):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"{self.value} -> {self.next}"

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
