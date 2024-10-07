'''
DFS Pseudocode

create a stack S
mark vertex as visited and place vertex into stack
while Q is not empty
    pop the top of the vertex V of the stack Q
    mark and enqueue all (unvisted) neighbors of vertex V

Time complexity:    O(N*N)
Space complexity:   O(N)
'''

from collections import deque

def dfs(adjacency_matrix: list, start: int):

    # Create a stack
    stack = deque()
    # Create a set for visited vertices
    visited = set()
    # Mark the starting vertex as visited
    visited.add(start)
    # Add the starting vertex to the stack
    stack.append(start)

    # While the stack is not empty
    while stack:
        # From the top of the stack
        vertex = stack.pop()
        print(str(vertex) + " ", end="")

        # Visit all the neighbors of the vertex
        for i in range(len(adjacency_matrix)):
            # If the neighbor has not been visited
            if (adjacency_matrix[vertex][i] == 1 and i not in visited):
                # Mark the neighbor as visited
                visited.add(i)
                # Add the neighbor to the stack
                stack.append(i)


if __name__ == '__main__':
    matrix = [[0, 1, 1, 0, 1, 0, 0],
              [1, 0, 0, 0, 0, 0, 0],
              [1, 0, 0, 0, 0, 1, 1],
              [0, 1, 1, 0, 0, 0, 1],
              [0, 1, 1, 0, 0, 1, 0],
              [1, 0, 1, 0, 1, 0, 0],
              [0, 0, 1, 1, 0, 0, 0]]

    print("DFS traversal: ")
    dfs(matrix, 0)