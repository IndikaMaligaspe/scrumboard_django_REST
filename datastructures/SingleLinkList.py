class Node:
    def __init__(self, data=None):
        self.data = data
        self.nextval = None


class SingleLinkedList:
    def __init__(self):
        self.headval = None
    
    
    def traversList(self):
        currval = self.headval;
        while currval is not None:
            print(currval.data)
            currval = currval.nextval
    

    def addAtBeginning(self, newdata):
        newNode = Node(newdata)
        newNode.nextval = self.headval
        self.headval = newNode
    
    
    def addAtEnd(self, newdata):
        newNode = Node(newdata)
        if self.headval == None:
            self.headval = newNode
            return
        last = self.headval
        while (last.nextval):
            last = last.nextval
        last.nextval = newNode


if __name__ == "__main__":
    list = SingleLinkedList()
    list.headval = Node("February")
    secondElement = Node("March")
    list.headval.nextval = secondElement
    thirdElement = Node("April")
    secondElement.nextval = thirdElement
    list.addAtBeginning("January")
    list.addAtEnd("May")
    list.traversList()

