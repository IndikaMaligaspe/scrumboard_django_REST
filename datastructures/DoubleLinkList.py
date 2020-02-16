class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def push(self,  data):
        newNode = Node(data)
        newNode.next = self.head
        if self.head is not None:
            self.head.prev = newNode
        self.head = newNode
        self.size = self.size+1

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
            self.size = self.size+1


    def append(self, data):
        newNode = Node(data)
        newNode.next = None
        if self.head is None:
            self.head = newNode
            newNode.prev = None
        
        node = self.head
        while (node is not None):
            last = node
            node = node.next
        last.next = newNode
        newNode.prev =  last
        self.size = self.size+1

        
    def remove(self, data):
        if self.head is None:
            print("Empty list.")
            return 
        removeNode = Node(data)
        node = self.head
        while (node is not None):
            if node.data == removeNode.data:
                if node.prev is None:
                    self.head = node.next
                    node.next.prev = None
                    self.size = self.size-1
                elif node.next is None:
                    node.prev.next = None    
                    self.size = self.size-1
                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    self.size = self.size-1
            last = node
            node = node.next


    def printlist(self):
        node = self.head
        while (node is not None):
            print(node.data)
            last = node
            node = node.next

if __name__ == "__main__":
    dlist = DoubleLinkList ()
    dlist.push(10)
    print("----------printing init----- size {:1}".format(dlist.size))
    dlist.printlist()
    dlist.push(20)
    dlist.push(30)
    print("----------printing again----- size {:1}".format(dlist.size))
    dlist.printlist()
    dlist.insert(dlist.head.next, 13)
    print("----------After Insert----- size {:1}".format(dlist.size))
    dlist.printlist()
    dlist.append(33)
    print("----------After 1st Append----- size {:1}".format(dlist.size))
    dlist.printlist()
    dlist.append(35)
    print("---------After 2nd Append----- size {:1}".format(dlist.size))
    dlist.printlist()
    dlist.remove(13)
    print("----------After Removing middle----- size {:1}".format(dlist.size))
    dlist.printlist()
    dlist.remove(35)
    print("----------After Removing last----- size {:1}".format(dlist.size))
    dlist.printlist()    
    dlist.remove(30)
    print("----------After Removing head----- size {:1}".format(dlist.size))
    dlist.printlist()    
