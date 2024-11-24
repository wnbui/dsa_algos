"""
LeetCode Questions
79 - Word search
207 - Course schedule
994 - Rotting oranges
417 - Pacific Atlantic water flow
127 - Word ladder
"""

"""
DFS for a graph represented as an adjacency list
"""

def dfs(graph):
    visited = set()
    result = []

    def explore(node):
        visited.add(node)
        result.append(node) # Process node
        for neighbor in graph[node]:
            if node not in visited:
                explore(neighbor)

    def dfs_driver(graph):
        for node in graph:
            if node not in visited:
                explore(node)

    dfs_driver()
    return result


"""
BFS for a graph represented as an adjacency list
"""

from collections import deque

def bfs(graph, start):
    visited = set()
    result = []

    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node) # Process node
            for neighbor in graph[node]:
                queue.append(neighbor)

    return result


"""
Topological sort only works on DAG graphs with no cycles
"""

def topological_sort(graph):
    visited = set()
    topo_order = []

    def has_cycle(node, curpath):
        visited.add(node)
        curpath.add(node)

        for neighbor in graph[node]:
            if neighbor in curpath: # cycle detected, no topo sort
                return True
            if neighbor in visited:
                continue
            if has_cycle(neighbor, curpath):
                return True
            
        curpath.remove(node)
        topo_order.append(node) # Process node
        return False
    
    for node in graph:
        if node not in visited:
            if has_cycle(node, set()):
                return None # Cycle detected, no topo sort
            
    # Reverse to get the correct topological order
    return topo_order[::-1]


"""
DFS for a matrix, visiting all connected cells
"""

def dfs_matrix(matrix):
    m, n = len(matrix), len(matrix[0])
    visited = set()
    result = []

    def explore(i, j):
        if not (0 <= i < m and 0 <= j < n):
            return
        if ((i,j)) in visited:
            return
        visited.add((i,j))
        result.append(matrix[i][j])  # process the cell

        # Explore neighbors (up, down, left, right)
        for deltaI, deltaJ in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            explore(i + deltaI, j + deltaJ)

    def dfs_driver():
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited:
                    explore(i, j)

    dfs_driver()
    return result


"""
BFS for a matrix, visiting all connected cells
"""

from collections import deque
def bfs_matrix(matrix, startI, startJ):
    m, n = len(matrix), len(matrix[0])
    visited = set()
    result = []

    queue = deque([(startI,startJ)])
    while queue:
        i, j = queue.popleft()
        if not (0 <= i < m and 0 <= j < n):
            continue
        if ((i,j)) in visited:
            continue
        visited.add((i,j))
        result.append(matrix[i][j])  # process the cell

        # Enqueue neighbors (up, down, left, right)
        for deltaI, deltaJ in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            queue.append((i + deltaI, j + deltaJ))
    
    return result