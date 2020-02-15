class Node:
    def __init__(self, data=None):
        self.data = data
        self.nextNode = None


class SingleLinkedList:
    def __init__(self):
        self.headval = None
    
    
    def traversList(self):
        currval = self.headval;
        while currval is not None:
            print(currval.data)
            currval = currval.nextNode
    

    def addAtBeginning(self, newdata):
        newNode = Node(newdata)
        newNode.nextNode = self.headval
        self.headval = newNode
    
    
    def addAtEnd(self, newdata):
        newNode = Node(newdata)
        if self.headval == None:
            self.headval = newNode
            return
        last = self.headval
        while (last.nextNode):
            last = last.nextNode
        last.nextNode = newNode

    
    def addAt(self, atnode, newnode):
        if atnode is None:
            print ("At Node is not avaibla ..")
            return
        newNode = Node(newnode)
        newNode.nextNode = atnode.nextNode
        atnode.nextNode = newNode
        
    def popElem(self, key):
        headVal =  self.headval
        if headVal is None:
            print("list empty already...")
            return
        if headVal.data == key:
            self.headval  = headVal.nextNode
            headVal = None
            return
        while(headVal is not None):
            if headVal.data == key:
                break
            prev = headVal
            headVal = headVal.nextNode

        if (headVal is None):
            print("Key not found...")
            return        

        prev.nextNode = headVal.nextNode
        headVal = None


if __name__ == "__main__":
    list = SingleLinkedList()
    list.headval = Node("February")
    secondElement = Node("March")
    list.headval.nextNode = secondElement
    thirdElement = Node("April")
    secondElement.nextNode = thirdElement
    list.traversList()
    print("--------------------------")

    list.addAtBeginning("January")
    list.traversList()
    print("--------------------------")

    list.addAtEnd("May")
    list.traversList()
    print("--------------------------")

    list.addAt(thirdElement,"April 14 - New Year day")
    list.traversList()
    print("--------------------------")
    list.popElem("April 14 - New Year day")
    print("--------------------------")
    list.traversList()
    list.popElem("August")
    print("------removing head----------")
    list.popElem("January")
    list.traversList()
