'''
Operations
- Heapify
- Build heap
- Insert
- Delete
- Merge
- Root
'''

def parent(index: int) -> int:
    return (index - 1) // 2


def left_child(index: int) -> int:
    return 2 * index + 1


def right_child(index: int) -> int:
    return 2 * index + 2
    

def min_heapify(heap: list, num: int, index: int):
    smallest = index
    left = left_child(index)
    right = right_child(index)

    if left < num and heap[left] < heap[smallest]:
        smallest = left

    if right < num and heap[right] < heap[smallest]:
        smallest = right

    if smallest != index:
        heap[smallest], heap[index] = heap[index], heap[smallest]
        min_heapify(heap, num, smallest)


def max_heapify(heap: list, num: int, index: int):
    largest = index
    left = left_child(index)
    right = right_child(index)

    if left < num and heap[left] > heap[largest]:
        largest = left

    if right < num and heap[right] > heap[largest]:
        largest = right

    if largest != index:
        heap[largest], heap[index] = heap[index], heap[largest]
        max_heapify(heap, num, largest)


def max_delete(heap: list, num: int) -> int:

    root = heap[0]
    heap[0] = heap[num - 1]
    num -= 1
    heap.pop()
    max_heapify(heap, num, 0)

    return root


def min_delete(heap: list, num: int) -> int:

    root = heap[0]
    heap[0] = heap[num - 1]
    num -= 1
    heap.pop()
    min_heapify(heap, num, 0)

    return root


def max_insert(heap: list, num: int):
    
    heap.append(num)
    print(len(heap))
    size = len(heap)
    max_heapify(heap, size, 0)


def min_insert(heap: list, num: int):

    heap.append(num)
    size = len(heap)
    min_heapify(heap, size, 0)


def build_min_heap(heap: list, num: int):
    
    start_index = num // 2 - 1

    for i in range(start_index, -1, -1):
        min_heapify(heap, num, i)


def build_max_heap(heap: list, num: int):
    
    start_index = num // 2 - 1

    for i in range(start_index, -1, -1):
        max_heapify(heap, num, i)


if __name__ == '__main__':

    arr = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9]
    n = len(arr)

    arr2 = [10, 5, 3, 2, 4]
    n2 = len(arr2)

    # arr3 = min_delete(arr2, n2)

    # build_min_heap(arr, n)
    # build_max_heap(arr2, n2)

    max_insert(arr2, 15)
    print(arr2)
    #print(arr3)