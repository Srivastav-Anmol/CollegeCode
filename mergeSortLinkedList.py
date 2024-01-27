class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def merge_sort(head):
    if head is None or head.next is None:
        return head

    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None

    left = merge_sort(head)
    right = merge_sort(next_to_middle)

    sorted_list = merge(left, right)
    return sorted_list


def merge(left, right):
    if left is None:
        return right
    if right is None:
        return left

    result = None

    if left.data <= right.data:
        result = left
        result.next = merge(left.next, right)
    else:
        result = right
        result.next = merge(left, right.next)

    return result


def get_middle(head):
    if head is None:
        return head

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def print_list(head):
    if head is None:
        print("Linked list is empty")
        return

    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")


# Example usage
# Creating a linked list
head = Node(6)
node2 = Node(2)
node3 = Node(9)
node4 = Node(3)
node5 = Node(5)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Original Linked List:")
print_list(head)

# Sorting the linked list using Merge Sort
head = merge_sort(head)

print("\nSorted Linked List:")
print_list(head)
