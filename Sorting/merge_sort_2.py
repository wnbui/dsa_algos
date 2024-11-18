"""
Merge sort passing array, low, and high.
Does not return an object as it sorts in place.
"""

def merge(array: list[int], low: int, mid: int, high: int):
    # Temporary sorted array
    temp = []
    # Starting idx of left half of array
    left = low
    # Starting idx of right half of array
    right = mid + 1

    # Until either left half or right half reaches the end
    while left <= mid and right <= high:
        # If left element is less than right element
        if array[left] < array[right]:
            temp.append(array[left])
            left += 1
        # If right element is less than left element
        else:
            temp.append(array[right])
            right += 1

    # Appending remaining elements of left half
    while left <= mid:
        temp.append(array[left])
        left += 1

    # Appending remaining elements of right half
    while right <= high:
        temp.append(array[right])
        right += 1

    # Copy temp array into array from low to high + 1
    for i in range(low, high + 1):
        array[i] = temp[i - low]


def merge_sort(array: list[int], low: int, high: int):
    if low < high:
        # 
        mid = (low + high) // 2
        merge_sort(array, low, mid) # Merge sort left half (low to mid)
        merge_sort(array, mid + 1, high) # Merge sort right half (mid + to high)
        merge(array, low, mid, high) # Merge sorted half


if __name__ == "__main__":
    array1 = [1, 4, 5, 6, 5, 3, 5, 7, 2]
    array2 = [2, 4, 1, 3, 5]

    merge_sort(array1, 0, len(array1) - 1)
    print(array1)
    merge_sort(array2, 0, len(array2) - 1)
    print(array2)
    # print(count_inversions(array1))
    # print(count_inversions(array2))
