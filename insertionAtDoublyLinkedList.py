class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class linkedList:
    def __init__(self):
        self.head=None
        self.tail=self.head
    def insertAtBegin(self,data):
        newNode=node(data)
        if self.head==None:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head.prev=newNode
            self.head=newNode

    def insertAtLast(self,data):
        newNode=node(data)
        if self.head==None:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode

    def insertAtPos(self,pos,data):
        newNode=node(data)
        if pos==1:
            newNode.next=self.head
            self.head=newNode
            self.tail=newNode
        else:
            temp=self.head
            for i in range(1,pos-1):
                if temp!=None:
                    temp=temp.next
            if temp!=None:
                newNode.next=temp.next
                temp.next.prev=newNode
                temp.next=newNode
                newNode.prev=temp

    def delAtBegin(self):
        if self.head==None:
            return
        else:
            temp=self.head
            temp.next.prev=None
            self.head=temp.next
            temp.next=None
    def delAtLast(self):
        current=self.head
        while(current.next!=None):
            previ=current
            current=current.next

       
        current.prev=None
        previ.next=None

    def delAtPos(self,pos):
        if pos==1:
            self.delAtBegin()
        else:
            temp=self.head
            for i in range(1,pos):
                current=temp
                temp=temp.next
            if temp!=None:
                current.next=temp.next
                temp.next.prev=current

    def printlist(self):
        cur=self.head
        while(cur!=None):
            print(cur.data,end="-->")
            cur=cur.next
    def count(self):
        count=0
        temp=self.head
        while(temp!=None):
            count+=1
            temp=temp.next
        print("\n")
        print("Length of Linked List = ",count)
    

ll=linkedList()
#ll.insertAtBegin(3)
#ll.insertAtBegin(4)
ll.insertAtLast(3)
ll.insertAtLast(4)
ll.insertAtLast(5)
ll.insertAtPos(3,6)
ll.insertAtPos(4,8)
#ll.delAtBegin()
#ll.delAtLast()
ll.delAtPos(3)
ll.printlist()

#ll.count()










