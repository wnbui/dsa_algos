class Node:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.prev = prev_node
        self.next = next_node


def convert_to_list(array):

    head = Node(array[0])
    prev = head

    for i in range(1, len(array)):
        temp = Node(array[i], None, prev)
        prev.next = temp
        prev = temp

    return head


def print_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()


def reverse_list(head):
    # If list is empty or list is one node
        # Return head
    if head is None or head.next is None:
        return head
    
    current = head
    previous = None

    while current is not None:
        # Set prev pointer to curr's prev
        previous = current.prev
        # Swap next and prev pointers
        current.prev = current.next
        current.next = previous

        # Move to the next node, which is now prev
        current = current.prev

    # Last node of list is new head
    return previous.prev


def insert(num: int):
    pass


def delete(num: int):
    pass


if __name__ == "__main__":
    
    array = [0, 1, 2, 3, 4, 5]

    head = convert_to_list(array)

    print("Original Linked List: ", end="")
    print_list(head)

    head = reverse_list(head)
    print_list(head)