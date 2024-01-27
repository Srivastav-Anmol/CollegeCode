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
    
    def print(self):
        current=self.head
        if current==None:
            print("Empty")
        else:
            while(current!=None):
                print(current.data,"-->",end=" ")
                current=current.next
    
    def sortList(self):
        zeroHead = node(-1)
        zeroTail = zeroHead
        oneHead = node(-1)
        oneTail = oneHead
        twoHead = node(-1)
        twoTail = twoHead

        curr = self.head
        while curr!=None:

            value = curr.data

            if value == 0:
                zeroTail.next = curr
                zeroTail = curr
                
            elif value == 1:
                oneTail.next = curr
                oneTail= curr
            elif value == 2:
                twoTail.next = curr
                twoTail = curr
            
            curr = curr.next

        
        if oneHead.next!=None:
            zeroTail.next = oneHead.next
        else:
            zeroTail.next = twoHead.next

        oneTail.next = twoHead.next
        twoTail.next = None

        # setup head
        self.head = zeroHead.next

        # delete dummy nodes
        self.zeroHead=None
        self.oneHead=None
        self.twoHead=None

        return self.head


ll=LinkedList()
ll.insertAtEnd(1)
ll.insertAtEnd(0)

ll.insertAtEnd(1)
ll.insertAtEnd(0)
ll.insertAtEnd(1)
print("Unsorted list = ",end="")
ll.print()
ll.sortList()
print("\nSorted list = ",end="")
ll.print()

