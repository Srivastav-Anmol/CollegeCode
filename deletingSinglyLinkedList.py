class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None


    def insertAtBegin(self,data):
        newNode=node(data)
        newNode.next=self.head
        self.head=newNode

    def delAtBegin(self):
        temp=self.head
        self.head=self.head.next
        temp=None


    def delAtEnd(self):
        temp=self.head
        while(temp.next.next !=None):
            temp=temp.next
        #lastNode=temp.next
        temp.next=None
        #lastNode.next=None


    def delAtPos(self,pos):
        if pos==1:
            self.delAtBegin()
        else:
            temp=self.head.next
            prev=self.head
            for i in range(pos-2):
                temp=temp.next
                prev=prev.next
            prev.next=temp.next
            
            


    def print(self):
        current=self.head
        if current==None:
            print("Empty")
        else:
            while(current!=None):
                print(current.data,"-->",end=" ")
                current=current.next

ll=LinkedList()
ll.insertAtBegin(2)
ll.insertAtBegin(3)
ll.insertAtBegin(4)
#ll.delAtEnd()
#ll.delAtEnd()
ll.print()
ll.delAtPos(2)
ll.print()


