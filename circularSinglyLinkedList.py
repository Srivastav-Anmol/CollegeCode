class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedList:
    def __init__(self):
        self.tail=None
    def insert(self,ele,x):
        newNode=node(x)
        if self.tail==None:
            self.tail=newNode
            newNode.next=newNode
        else:
            curr=self.tail

            while(curr.data!=ele):
                curr=curr.next
            """ element found """ 
            temp=newNode
            temp.next=curr.next
            curr.next=temp  
    def printl(self):
        
        temp=self.tail
        while(temp.next!=temp):
            print(temp.data,end="-->")
            temp=temp.next
ll=linkedList()
ll.insert(3,5)
ll.insert(3,4)
ll.printl()

