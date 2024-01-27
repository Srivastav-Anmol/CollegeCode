class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.random = None


class Solution:
    def insertAtTail(self, head, tail, d):
        newNode = Node(d)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
        return head, tail

    def copyList(self, head):
        cloneHead = None
        cloneTail = None
        temp = head
        while temp is not None:
            cloneHead, cloneTail = self.insertAtTail(cloneHead, cloneTail, temp.data)
            temp = temp.next

        oldToNewNode = {}
        originalNode = head
        cloneNode = cloneHead
        while originalNode is not None:
            oldToNewNode[originalNode] = cloneNode
            originalNode = originalNode.next
            cloneNode = cloneNode.next

        originalNode = head
        cloneNode = cloneHead
        while originalNode is not None:
            if originalNode.random is not None:
                cloneNode.random = oldToNewNode[originalNode.random]
            else:
                cloneNode.random = None
            originalNode = originalNode.next
            cloneNode = cloneNode.next

        return cloneHead

    def printList(self, head):
        while head is not None:
            print(head.data, end="-->")
            head = head.next
        print("None")

    def print_random(self, head):
        while head is not None:
            print(head.data, end="-->")
            if head.random is not None:
                print(head.random.data, end="-->")
            head = head.next


if __name__ == "__main__":
    ll = Solution()
    head = Node(1)
    
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.random=head.next.next

    print("Original Linked List:")
    ll.printList(head)

    cloned_head = ll.copyList(head)

    print("Cloned Linked List:")
    ll.printList(cloned_head)

    print("Original Linked List Random Pointers:")
    ll.print_random(head)

    print("\nCloned Linked List Random Pointers:")
    ll.print_random(cloned_head)
