import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Create the metro station network graph
G = nx.Graph()
stations = ['Station 1', 'Station 2', 'Station 3', 'Station 4', 'Station 5',
            'Station 6', 'Station 7', 'Station 8', 'Station 9', 'Station 10']
G.add_nodes_from(stations)
connections = [('Station 1', 'Station 2', {'weight': 3}), 
               ('Station 2', 'Station 3', {'weight': 5}), 
               ('Station 3', 'Station 4', {'weight': 2}), 
               ('Station 4', 'Station 5', {'weight': 4}), 
               ('Station 5', 'Station 6', {'weight': 1}), 
               ('Station 6', 'Station 7', {'weight': 6}), 
               ('Station 7', 'Station 8', {'weight': 2}), 
               ('Station 8', 'Station 9', {'weight': 3}), 
               ('Station 9', 'Station 10', {'weight': 4}), 
               ('Station 1', 'Station 5', {'weight': 2}), 
               ('Station 2', 'Station 8', {'weight': 3}), 
               ('Station 3', 'Station 9', {'weight': 1}), 
               ('Station 4', 'Station 10', {'weight': 5})]
G.add_edges_from(connections)

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, attrs in graph[current_node].items():
            weight = attrs.get('weight', 1) 
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Visualize the graph with weights
pos = nx.spring_layout(G) 
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=12, font_weight='bold')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Metro Station Network Graph with Weights")
plt.show()

graph_dict = nx.to_dict_of_dicts(G)

shortest_paths = {}
for station in G.nodes:
    shortest_paths[station] = dijkstra(graph_dict, station)

print("Shortest paths from each station to all others:")
for station in G.nodes:
    print(f"Paths from station {station}:")
    for dest, distance in shortest_paths[station].items():
        if distance != float('inf'):
            if station != dest:
                path_length = len(nx.shortest_path(G, station, dest)) - 1
                print(f"  {dest}: {path_length} stations (the distance = {distance})")
    print()
