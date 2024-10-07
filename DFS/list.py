'''
DFS Pseudocode

create a stack S
mark vertex as visited and place vertex into stack
while Q is not empty
    pop the top of the vertex V of the stack Q
    mark and enqueue all (unvisted) neighbors of vertex V

Time complexity:    O(V*E) where V = vertices & E = edges
Space complexity:   O(N)
'''

from collections import deque

def DFS(adjacency_list, start):

    # Create a stack
    stack = deque()
    # Create a set for visited vertices
    visited = set()
    # Mark the sarting vertex as visited
    visited.add(start)
    # Add starting vertex to the stack
    stack.append(start)

    # While the stack is not empty
    while stack:
        # From the top of the stack
        vertex = stack.pop()
        print(str(vertex) + " ", end="")

        # Visit all the neighbors of the vertex
        for neighbor in adjacency_list[vertex]:
            # If the neighbor has not been visited
            if neighbor not in visited:
                # Mark neighbor as visited
                visited.add(neighbor)
                # Add neighbor to the stack
                stack.append(neighbor)


if __name__ == '__main__':
    graph = {0: [1, 2, 4],
             1: [0],
             2: [0, 4, 5, 6],
             3: [6],
             4: [0, 5],
             5: [2, 4],
             6: [2, 3]}

    print("DFS traversal: ")
    DFS(graph, 0)