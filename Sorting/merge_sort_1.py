"""
Merge sort passing only an array.
Returns array.
"""

def merge(left: list[int], right: list[int]) -> list[int]:
    sorted_arr = []
    i = j = 0

    # Merge to arrays while maintaining ascending order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    
    # Append any remaining elements in left or right halves
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    
    return sorted_arr


def merge_sort(array: list[int]):
    # Base case: array of length 1
    if len(array) == 1:
        return array
    
    # Divide the array into two halves and recursively call
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    # Merge both sorted halves
    return merge(left, right)


if __name__ == "__main__":
    array1 = [1, 4, 5, 6, 5, 3, 5, 7, 2]
    array2 = [2, 4, 1, 3, 5]

    print(merge_sort(array1))
    print(merge_sort(array2))
    # print(count_inversions(array1))
    # print(count_inversions(array2))
