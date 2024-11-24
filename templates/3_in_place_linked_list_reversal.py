"""
LeetCode Questions
206 - Reverse linked list
143 - Reorder list
25 - Reverse nodes in k-group
"""

"""
A generic template for in place linked list reversal
"""

def reverse_linked_list(head):
    prev = None
    cur = head

    while cur:
        # Save the next node
        next_node = cur.next

        # Reverse the current node's pointer
        cur.next = prev

        # Move the pointers one step forward
        prev = cur
        cur = next_node

    # prev is the new head after the loop ends
    return prev
