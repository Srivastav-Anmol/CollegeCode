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

        
    def insertAtEnd(self,data):
        newNode = node(data)
        if self.head==None:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode 

    def insertAtPosition(self,pos,data):
        newNode=node(data)
        if pos==1:
            newNode.next=self.head
            self.head=newNode
        else:
            temp=self.head
            count=1
            while(temp!=None and count<(pos-1)):
                temp=temp.next
                count+=1
            newNode.next=temp.next
            temp.next=newNode
            

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
ll.insertAtPosition(1,4)
ll.print()
