def pivoted_search(array: list[int], value) -> int:
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (right + left) // 2

        # If value is found
        if array[mid] == value:
            return mid
        # If left half is sorted
        if array[mid] >= array[left]:
            if array[left] <= value and array[mid]:
                right = mid -1
            else:
                left = mid + 1
        # If right half is sorted
        else:
            if array[mid] < value and value <= array[right]:
                right = mid - 1
            else:
                left = mid + 1

    return -1
                


if __name__ == "__main__":
    # Driver code
    arr1 = [4, 5, 6, 7, 0, 1, 2]
    key1 = 0
    result1 = pivoted_search(arr1, key1)
    print(result1)  # Output: 4

    arr2 = [4, 5, 6, 7, 0, 1, 2]
    key2 = 3
    result2 = pivoted_search(arr2, key2)
    print(result2)  # Output: -1