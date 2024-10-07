'''
BFS Pseudocode

create a queue Q
mark vertex as visited and place vertex into Q
while Q is not empty
    pop the front vertex V of the queue Q
    mark and enqueue all (unvisted) neighbors of vertex V

Time complexity:    O(N*N)
Space complexity:   O(N)
'''

from collections import deque

def BFS(adjacency_matrix, start):

    # Create a queue
    queue = deque()
    # Create a set for visited vertices
    visited = set()
    # Mark the starting vertex as visited
    visited.add(start)
    # Add starting vertex to the queue
    queue.append(start)

    # While queue is not empty
    while queue:
        # From the front of the queue
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        # Visit all the neighbors of the vertex
        for i in range(len(adjacency_matrix)):
            # If the neighbor has not been visited
            if (adjacency_matrix[vertex][i] == 1 and i not in visited):
                # Mark neighbor as visited
                visited.add(i)
                # Add neighbor to the queue
                queue.append(i)


if __name__ == '__main__':
    matrix = [[0, 1, 1, 0, 1, 0, 0],
              [1, 0, 0, 0, 0, 0, 0],
              [1, 0, 0, 0, 0, 1, 1],
              [0, 1, 1, 0, 0, 0, 1],
              [0, 1, 1, 0, 0, 1, 0],
              [1, 0, 1, 0, 1, 0, 0],
              [0, 0, 1, 1, 0, 0, 0]]

    print("BFS traversal: ")
    BFS(matrix, 0)