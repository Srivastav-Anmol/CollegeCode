class node:
    def __init__(self,data):
        self.data=data
        self.head=None
class linkedList:
    def __init__(self):
        self.head=None


    def insertAtBegin(self,data):
        newNode=node(data)
        newNode.next=self.head
        self.head=newNode

    def rev(self):
        curr=self.head
        prev=None
        while(curr!=None):
            forw=curr.next
            curr.next=prev
            prev=curr
            curr=forw
        self.head=prev


    def middle(self):
        slow=self.head
        fast=self.head.next
        while(fast!=None):
            fast=fast.next
            if fast!=None:
                fast=fast.next
            slow=slow.next
        print("Middle = ",slow.data)

    


    def print(self):
        current=self.head
        if current==None:
            print("Empty")
        else:
            while(current!=None):
                print(current.data,"-->",end=" ")
                current=current.next
        
ll=linkedList()
ll.insertAtBegin(3)
ll.insertAtBegin(4)
ll.insertAtBegin(5)
ll.insertAtBegin(6)
ll.insertAtBegin(7)
ll.insertAtBegin(8)
ll.print()
print("\n")
ll.rev()
ll.print()
print("\n")
ll.middle()