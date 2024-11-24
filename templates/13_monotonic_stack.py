"""
LeetCode Questions
496 - Next greater element I
503 - Next greater element II
739 - Daily temperatures
84 - Largest rectangle in histogram
"""

"""
Monotonic increasing stack template
"""

def monotonic_increasing_stack(arr):
    stack = [] 
    for i, num in enumerate(arr):
        # Modify condition based on the problem
        while stack and stack[-1][0] > num:
            stack.pop()

        if stack:
            pass # process result from top of stack

        # Append current value and index
        stack.append((num,i))


"""
Monotonic decreasing stack template
"""

def monotonic_decreasing_stack(arr):
    stack = []
    for i, num in enumerate(arr):
        # Modify condition based on the problem
        while stack and stack[-1][0] < num:
            stack.pop()

        if stack:
            pass # process result from top of stack

        # Append current value and index
        stack.append((num,i))