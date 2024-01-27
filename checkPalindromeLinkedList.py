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



    """ def isPalindrome(self,arr):
        s=0
        e=len(arr)-1
        while(s<=e):
            if arr[s]!=arr[e]:
                return False
            else:
                s+=1
                e-=1
        return True


    def checkPalindrome(self):
        arr=[]
        temp=self.head
        while(temp!=None):
            arr.append(temp.data)
            temp=temp.next
        return self.isPalindrome(arr)"""
    
    def getmiddle(self):
        slow=self.head
        fast=self.head.next
        while(fast!=None and fast.next!=None):
            fast=fast.next.next
            slow=slow.next
        return slow
    
    def reverse(self,temp):
        curr=temp
        prev=None
        next=None

        while(curr!=None):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        
        return prev


    
    def palindrome(self):
        if self.head.next==None:
            return True
        #find middle of linked list
        middle=self.getmiddle()
        
        #reverse the linked list after mid node
        temp=middle.next
        middle.next=self.reverse(temp)

        #compare both halves
        head1=self.head
        head2=middle.next
        while(head2!=None):
            if head1.data!=head2.data:
                return False
            head1=head1.next
            head2=head2.next

        return True
    






ll=LinkedList()
ll.insertAtEnd(1)
ll.insertAtEnd(2)
ll.insertAtEnd(2)
ll.insertAtEnd(0)
ll.print()
print()
if ll.palindrome():
    print("Palindrome")
else:
    print("Not Palindrome")
