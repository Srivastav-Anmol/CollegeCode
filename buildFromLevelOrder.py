import collections
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.Right=None
    def build(self):
        q=collections.deque()
        data=int(input("Enter data for root "))
        root=node(data)
        q.append(root)
        while q:
            temp=q[0]
            q.popleft()
            print("Enter left node ",temp.data)
            leftdata=int(input())
            if leftdata!=-1:
                temp.left=node(leftdata)
                q.append(temp.left)
            print("Enter right node ",temp.data )
            rightdata=int(input())
            if rightdata!=-1:
                temp.right=node(rightdata)
                q.append(temp.right)
p=node(1)
p.build()