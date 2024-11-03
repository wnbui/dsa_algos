class Node:
    def __init__(self, data, next_node = None):
        self.data = data
        self.next = next_node


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
        print(curr.data, end=" ")
        curr = curr.next
    print()

def reverse_list(head):
    pass

def insert(num: int):
    pass

def delete(num: int):
    pass


if __name__ == "__main__":
    
    array = [0, 1, 2, 3, 4, 5]

    head = convert_to_list(array)
    
    print("Original Linked List: ", end="")
    print_list(head)