'''
BFS Pseudocode

create a queue Q
mark vertex as visited and place vertex into Q
while Q is not empty
    pop the front vertex V of the queue Q
    mark and enqueue all (unvisted) neighbors of vertex V

Time complexity:    O(V*E) where V = vertices & E = edges
Space complexity:   O(N)
'''

from collections import deque

def bfs(adjacency_list: list, start: int):

    # Create a queue
    queue = deque()
    # Create a set for visited vertices
    visited = set()
    # Mark the starting vertex as visited
    visited.add(start)
    # Add starting vertex to the queue
    queue.append(start)

    # While the queue is not empty
    while queue:
        # From the front of the queue
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        # Visit all the neighbors of the vertex
        for neighbor in adjacency_list[vertex]:
            # If the neighbor has not beed visited
            if neighbor not in visited:
                # Mark neighbor as visited
                visited.add(neighbor)
                # Add neighbor to the queue
                queue.append(neighbor)


if __name__ == '__main__':
    graph = {0: [1, 2, 4],
             1: [0],
             2: [0, 4, 5, 6],
             3: [6],
             4: [0, 5],
             5: [2, 4],
             6: [2, 3]}

    print("BFS traversal: ")
    bfs(graph, 0)