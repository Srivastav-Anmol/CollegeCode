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

    def removeDuplicate(self):
        curr=self.head
        if self.head==None:
            return None
        while(curr!=None):
            if curr.next!=None and curr.data==curr.next.data:
                nextTonext=curr.next.next
                nodeToDelete=curr.next
                nodeToDelete=None
                curr.next=nextTonext
            else:
                curr=curr.next
        return curr

    
    def sortList(self):
        if self.head==None:
            return None
        temp=self.head
        while(temp!=None):
            i=temp.next
            while(i!=None):
                if(temp.data>i.data):
                    var=i.data
                    i.data=temp.data
                    temp.data=var
                i=i.next
            temp=temp.next
        return self.head
    
    def removeUnsorted(self):
        if self.head==None:
            return None
        temp=self.head
        s=set()
        while(temp!=None):
            if temp in s:
                next=temp.next
                temp.next=None
                temp=next
            s.add(temp)
            temp=temp.next
        return self.head




ll=LinkedList()
ll.insertAtEnd(2)
ll.insertAtEnd(6)

ll.insertAtEnd(1)
ll.insertAtEnd(8)
ll.insertAtEnd(7)
ll.print()
print()
#ll.removeDuplicate()
#ll.print()<!DOCTYPE html>


""" ll.sortList()
ll.print() """

ll.removeUnsorted()
ll.print()

