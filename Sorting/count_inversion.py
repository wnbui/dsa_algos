def merge(array: list[int], low: int, mid: int, high: int) -> int:
    sorted_array = []
    left = low
    right = mid + 1
    
    count = 0

    while left <= mid and right <= high:
        if array[left] < array[right]:
            sorted_array.append(array[left])
            left += 1
        else:
            sorted_array.append(array[right])
            count += (mid - left + 1)
            right += 1

    while (left <= mid):
        sorted_array.append(array[left])
        left += 1

    while (right <= high):
        sorted_array.append(array[right])
        right += 1

    for i in range(low, high + 1):
        array[i] = sorted_array[i - low]

    return count


def merge_sort(array: list[int], low: int, high: int) -> int:
    count = 0

    if low >= high:
        return count
    
    mid = (low + high) // 2
    count += merge_sort(array, low, mid)
    count += merge_sort(array, mid + 1, high)
    count += merge(array, low, mid, high)

    return count

def count_inversions(array: list[int]) -> int:
    n = len(array)

    return merge_sort(array, 0, n -1)


if __name__ == "__main__":
    a = [5, 4, 3, 2, 1]
    b = [2, 4, 1, 3, 5]
    cnt1 = count_inversions(a)
    cnt2 = count_inversions(b)
    print("The number of inversions are:", cnt1)
    print("The number of inversions are:", cnt2)
