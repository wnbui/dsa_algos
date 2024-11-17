class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


def convert_to_list(array):
    head = Node(array[0])
    curr = head

    for i in range(1, len(array)):
        temp = Node(array[i], None)
        curr.next = temp
        curr = temp

    return head


def print_list(head):
    curr = head
    while curr is not None:
        print(curr.value, end=" ")
        curr = curr.next
    print()


def reverse_list(head):
    pass


def insertHead(value: int):
    pass


def insertTail(value: int):
    pass

def remove(head: Node, value: int):
    # Case of empty list
    if head is None:
        return head
    
    # Case of first node
    current = head
    if current.value == value:
        temp = current
        current = current.next
        del temp

        return current

    # Case of node in the middle or last or value not in list
    current = head.next
    previous = head

    while current is not None:
        # If the value is found
        if current.value == value:
            # From current, connect previous node to next node
            temp = current
            previous.next = current.next
            # Delete node
            del temp
        # Else not value
        else:
            previous = current
        current = current.next
    
    return head


def getValues(head: Node) -> list:
    pass


if __name__ == "__main__":
    
    array = [0, 1, 2, 3, 4, 5]

    head = convert_to_list(array)
    
    print("Original Linked List: ", end="")
    print_list(head)

    head = remove(head, 2)

    print_list(head)