"""
LeetCode Questions
104 - Maximum depth of binary tree
102 - Binary tree level order traversal
105 - Construct binary tree from preorder and inorder traversal
124 - binary tree maximum path sums
"""

"""
Preorder traversal: visit node, then left subtree, then right subtree
"""

def preorder_traversal(node):
    if not node:
        return
    # visit node
    preorder_traversal(node.left)
    preorder_traversal(node.right)


"""
Inorder traversal: visit left subtree, then node, then right subtree
"""

def inorder_traversal(node):
    if not node:
        return
    inorder_traversal(node.left)
    # visit node
    inorder_traversal(node.right)


"""
Postorder traversal: visit left subtree, then right subtree, then node
"""

def postorder_traversal(node):
    if not node:
        return
    postorder_traversal(node.left)
    postorder_traversal(node.right)
    # visit node


"""
BFS traversal: visit all nodes level by level using a queue
"""

from collections import deque

def bfs_traversal(node):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            # visit node
            queue.append(node.left)
            queue.append(node.right)
