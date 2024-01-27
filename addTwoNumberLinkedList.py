class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def addTwoNumbers(self,l1,l2):
        dummy=node(0)
        curr=dummy
        carry=0
        while(l1!=None or l2!=None or carry!=0):
            if l1!=None:
                val1=l1.data
            else:
                val1=0
            if l2!=None:
                val2=l2.data
            else:
                val2=0
            total=val1+val2+carry
            carry=total//10
            digit=total%10

            curr.next=node(digit)
            curr=curr.next

            if l1!=None:
                l1=l1.next
            else:
                l1=None
            if l2!=None:
                l2=l2.next
            else:
                l2=None
        
        return dummy.next
    

    def print(self,head):
        current=head
        if current==None:
            print("Empty")
        else:
            while(current!=None):
                print(current.data,"-->",end=" ")
                current=current.next
ll=LinkedList()
h1=node(2)
h1.next=node(3)
h1.next.next=node(3)
print("First linked list = ",end="")
ll.print(h1)
print()
h2=node(5)
h2.next=node(4)
h2.next.next=node(3)
print("Second linked list = ",end="")
ll.print(h2)
print()
a=ll.addTwoNumbers(h1,h2)
print("Addition of Two linked list = ",end="")
ll.print(a)