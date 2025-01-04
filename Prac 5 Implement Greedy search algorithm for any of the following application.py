import heapq

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        # Add an edge to the graph
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # Assuming an undirected graph

    def dijkstra(self, source):
        # Initialize distances and visited array
        distances = [float('inf')] * self.vertices
        distances[source] = 0
        visited = [False] * self.vertices

        # Priority queue to select the next vertex with the minimum distance
        min_heap = [(0, source)]

        while min_heap:
            # Get the vertex with the minimum distance
            dist, u = heapq.heappop(min_heap)

            if visited[u]:
                continue

            visited[u] = True

            for v, weight in self.graph[u]:
                if not visited[v] and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    heapq.heappush(min_heap, (distances[v], v))

        return distances

# Example usage:
if __name__ == "__main__":
    # Create a weighted graph
    vertices = 6
    g = Graph(vertices)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 3)
    g.add_edge(1, 2, 1)
    g.add_edge(1, 3, 2)
    g.add_edge(2, 3, 4)
    g.add_edge(3, 4, 2)
    g.add_edge(4, 5, 6)

    source = 0  # Source vertex
    shortest_distances = g.dijkstra(source)

    print("Shortest Distances from Source Vertex {}: ".format(source))
    for vertex, distance in enumerate(shortest_distances):
        print("Vertex {}: Distance = {}".format(vertex, distance))
