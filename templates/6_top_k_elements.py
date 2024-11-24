"""
LeetCode Questions
215 - Kth largest element in an array
347 - Top k frequent elements
23 - Merge k sorted lists
"""

"""
A generic template for the top k largest elements
"""

import heapq

def top_k_largest_element(arr, k):
    if k <= 0 or not arr:
        return []
    
    # Use a max heap to maintain the k smallest elements
    max_heap = []

    for num in arr:
        # Python does not have a max heap, only a min heap
        # Therefore, negate the num to simulate a max heap
        heapq.heappush(max_heap, -num)
        if len(max_heap) > k:
            heapq.heappop(max_heap)

    # Convert back to positive values and return
    return [-x for x in max_heap]

"""
A generic template for the top k smallest elements 
"""

import heapq

def top_k_smallest_element(arr, k):
    if k <= 0 or not arr:
        return []
    
    # Use a min heap to maintain the k largest elements
    min_heap = []

    for num in arr:
        heapq.headpush(min_heap, num)
        if len(min_heap) > k:
            heapq.headpop(min_heap)

    return min_heap