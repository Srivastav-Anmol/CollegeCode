class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def insertAtEnd(self,data):
        newNode = node(data)
        if self.head==None:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode
    def createLoop(self):
        self.tail.next=self.head.next
    

    """ def checkLoop(self):
        contain=set()
        temp=self.head
        while(temp!=None):
            if temp in contain:
                return True
            contain.add(temp)
            temp=temp.next
        return False """

    def floydCheck(self):
        if self.head==None:
            return False
        slow=self.head
        fast=self.head
        while(slow!=None and fast!=None):
            fast=fast.next
            if fast!=None:
                fast=fast.next
            slow=slow.next
            if slow==fast:
                return slow
        return None
    
    def startNode(self):
        if self.head==None:
            return None
        intersectionPoint=self.floydCheck()
        self.slow=self.head
        while(self.slow!=intersectionPoint):

            self.slow=self.slow.next
            intersectionPoint=intersectionPoint.next
        
        return (self.slow)


    def removeLoop(self):
        if self.head==None:
            return
        self.startOfLoop=self.startNode()
        temp=self.startOfLoop
        while(temp.next!= self.startOfLoop):
            temp=temp.next
        temp.next=None
        print("Loop is removed")





    def print(self):
        current=self.head
        if current==None:
            print("Empty")
        else:
            while(current!=None):
                print(current.data,"-->",end=" ")
                current=current.next

ll=LinkedList()
ll.insertAtEnd(2)
ll.insertAtEnd(3)

ll.insertAtEnd(5)
ll.insertAtEnd(6)
ll.insertAtEnd(7)
ll.createLoop()
if ll.floydCheck():
    print("Loop is present")
else:
    print("Loop is not present")
print()
print("Starting node in loop = ",ll.startNode().data)
print()
ll.removeLoop()
ll.print()