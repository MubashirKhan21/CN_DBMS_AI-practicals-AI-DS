from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs_recursive(self, v, visited):
        visited[v] = True
        print(v, end=' ')

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs_recursive(neighbor, visited)

    def dfs(self, start_vertex):
        visited = [False] * len(self.graph)
        print("Depth-First Search (DFS):")
        self.dfs_recursive(start_vertex, visited)
        print()

    def bfs(self, start_vertex):
        visited = [False] * len(self.graph)
        queue = []

        visited[start_vertex] = True
        queue.append(start_vertex)

        print("Breadth-First Search (BFS):")
        while queue:
            v = queue.pop(0)
            print(v, end=' ')

            for neighbor in self.graph[v]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        print()

# Create a sample graph
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 4)
g.add_edge(3, 4)

# Perform DFS and BFS starting from vertex 0
g.dfs(0)
g.bfs(0)
