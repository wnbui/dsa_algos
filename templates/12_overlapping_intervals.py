"""
LeetCode Questions
57 - Insert interval
56 - Merge interval
435 - Non-overlapping intervals
1834 - Single-threaded CPU
"""

"""
Generic template for interval problems
"""

def process_intervals(intervals):
    # Sort intervals by start time (common preprocessing step)
    intervals.sort(key=lambda x: x[0])
    
    # Example: Merged intervals (modify as needed for your problem)
    result = []
    for interval in intervals:
        # If result is empty or no overlap with the last interval in result
        if not result or result[-1][1] < interval[0]:
            result.append(interval)  # Add the interval as is
        else:
            # Merge overlapping intervals
            result[-1][1] = max(result[-1][1], interval[1])
    
    return result