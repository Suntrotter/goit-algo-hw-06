import networkx as nx
import timeit

# Function to perform Depth-First Search (DFS)
def dfs_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph.neighbors(start):
        if node not in path:
            new_paths = dfs_paths(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths

# Function to perform Breadth-First Search (BFS)
def bfs_paths(graph, start, end):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next_node in graph.neighbors(vertex):
            if next_node not in path:
                if next_node == end:
                    yield path + [next_node]
                else:
                    queue.append((next_node, path + [next_node]))

# Create the metro station network graph
G = nx.Graph()
stations = ['Station 1', 'Station 2', 'Station 3', 'Station 4', 'Station 5',
            'Station 6', 'Station 7', 'Station 8', 'Station 9', 'Station 10']
G.add_nodes_from(stations)
connections = [('Station 1', 'Station 2'), ('Station 2', 'Station 3'), 
               ('Station 3', 'Station 4'), ('Station 4', 'Station 5'), 
               ('Station 5', 'Station 6'), ('Station 6', 'Station 7'), 
               ('Station 7', 'Station 8'), ('Station 8', 'Station 9'), 
               ('Station 9', 'Station 10'), ('Station 1', 'Station 5'), 
               ('Station 2', 'Station 8'), ('Station 3', 'Station 9'), 
               ('Station 4', 'Station 10')]
G.add_edges_from(connections)

start_station = 'Station 1'
end_station = 'Station 10'

dfs_paths_list = dfs_paths(G, start_station, end_station)

bfs_paths_list = list(bfs_paths(G, start_station, end_station))

print("DFS Paths:")
for path in dfs_paths_list:
    print(path)

print("\nBFS Paths:")
for path in bfs_paths_list:
    print(path)

# Measure execution time for DFS
dfs_time = timeit.timeit(lambda: dfs_paths(G, start_station, end_station), number=1000)
print("DFS Execution Time:", dfs_time)

# Measure execution time for BFS
bfs_time = timeit.timeit(lambda: list(bfs_paths(G, start_station, end_station)), number=1000)
print("BFS Execution Time:", bfs_time)
