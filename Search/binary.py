def binary_search_iterative(array: list[int], value: int) -> int:
    left = 0
    right = len(array) - 1

    while left <= right:
        # Calculate the mid using left and right
        mid = (left + right) // 2
        # If value is mid, return mid
        if array[mid] == value:
            return mid
        # If value is in the right half, update left to mid + 1
        elif array[mid] < value:
            left = mid + 1
        # If value is in the left half, update right to mid - 1
        else:
            right = mid - 1

    # Value not found
    return -1


def binary_search_recursive(array: list[int], value) -> int:
    return binary_search_recursive_helper(array, value, 0, len(array) - 1)


def binary_search_recursive_helper(array: list[int], value: int, left: int, right) -> int:
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if array[mid] < value:
        return binary_search_recursive_helper(array, value, mid + 1, right)
    elif array[mid] > value:
        return binary_search_recursive_helper(array, value, left, mid - 1)
    else:
        return mid


if __name__ == "__main__":
    
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    value = 5

    print(binary_search_iterative(array, value))
    print(binary_search_recursive(array, value))
