"""
LeetCode Questions
303 - Range sum query - immutable
523 - Continuous subarray sum
560 - Subarray sum equals k
"""

"""
Builds the prefix sum array
"""

def build_prefix_sum(arr):
    # Initialize prefix sum array
    n = len(arr)
    prefix = [0] * n 

    # First element is the same as the original array
    prefix[0] = arr[0]

    # Build the prefix sum array
    for i in range(1, n):
        prefix[i] = prefix[i - 1] + arr[i]

    return prefix


"""
Queries the sum of elements in a subarray [left, right] using prefix sum
"""

def query_subarray_sum(prefix, i, j):
    if i == 0:
        return prefix[j]
    return prefix[j] - prefix[i - 1]