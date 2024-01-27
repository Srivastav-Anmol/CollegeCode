class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def merge_sorted_lists(head1, head2):
    dummy = Node(0)
    curr = dummy

    
    while head1!=None and head2!=None:
        if head1.data <= head2.data:
            curr.next = head1
            nextToHead1=head1.next
            
            head1=None
            head1=nextToHead1

        else:
            curr.next = head2
            nextToHead2=head2.next
            
            head2=None
            head2=nextToHead2
        curr = curr.next

    # Attach the remaining nodes of the non-empty list
    if head1==None:
        curr.next = head1
    elif head2==None:
        curr.next = head2

    return dummy.next


def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    print()


# Test the program
# Create the first sorted linked list: 1 -> 3 -> 5
head1 = Node(1)
head1.next = Node(3)
head1.next.next = Node(5)

# Create the second sorted linked list: 2 -> 4 -> 6
head2 = Node(2)
head2.next = Node(4)
head2.next.next = Node(6)

print("First Sorted Linked List:")
print_list(head1)

print("Second Sorted Linked List:")
print_list(head2)

merged_head = merge_sorted_lists(head1, head2)

print("Merged Sorted Linked List:")
print_list(merged_head)
