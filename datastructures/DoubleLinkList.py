class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkList:
    def __init__(self):
        self.head = None
    
    def push(self,  data):
        newNode = Node(data)
        newNode.next = self.head
        if self.head is not None:
            self.head.prev = newNode
        self.head = newNode

    def insert(self, prev , data):
        if prev is None:
            print("can not insert with None previous element")
            return
        
        newNode = Node(data)
        newNode.next = prev.next
        newNode.prev = prev
        prev.next = newNode
        if (newNode.next is not None):
            newNode.next.prev = newNode

    def printlist(self):
        node = self.head
        while (node is not None):
            print(node.data)
            last = node
            node = node.next

if __name__ == "__main__":
    dlist = DoubleLinkList ()
    dlist.push(10)
    print("----------printing init-----")
    dlist.printlist()
    dlist.push(20)
    dlist.push(30)
    print("----------printing again-----")
    dlist.printlist()
    dlist.insert(dlist.head.next, 13)
    print("----------After Insert-----")
    dlist.printlist()
