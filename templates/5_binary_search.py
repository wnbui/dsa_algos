"""
LeetCode Questions
34 - Find first and last position of element in sorted array
153 - Find minimum in rotated sorted array
33 - Search in rotated sorted array
"""

"""
Class binary search algorithm that infds a target value
"""

def classic_binary_search(array, target):
    left, right = 0, len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return - 1


"""
A generic template for binary search such that the returned value is the minimum index where condition(k) is true

Example 1:
array = [1,2,2,2,3]
target = 2
binary_search(array, lambda mid: array[mid] >= target) --> 1

Example 2:
array = [1,2,2,2,3]
target = 2
binary_search(array, lambda mid: array[mid] > target) --> 4
"""

def binary_search(array, condition):
    left, right = 0, len(array)

    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left


"""
Binary search algo that can search a rotated array by selecting the appropriate half to scan at each iteration
"""

def binary_search_rotated_array(array, target):
    left, right = 0, len(array) - 1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] == target:
            return mid
        
        # Left side sorted
        if array[left] <= array[mid]:
            # If target is contained in left sorted side, go left
            if array[left] <= target and array[left] <= array[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right side sorted
        else:
            # If target is contained in right sorted side, go right
            if array[mid] <= target and array[mid] <= array[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1