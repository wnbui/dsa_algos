"""
LeetCode Questions
141 - Linked list cycle
142 - Linked list cycle II
19 - Remove Nth node from end of list (double linked list)
"""

"""
A generic template for slow and fast pointers
"""

def slow_fast_pointers(head):
    # Initialize pointers
    slow = head
    fast = head
    result = None

    # Move slow once, move fast twice
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # Update result based on custom logic
        # Example: if fast == slow then cycle is detected

    return result