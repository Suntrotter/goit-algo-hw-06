import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# Add 10 metro stations as nodes
stations = ['Station 1', 'Station 2', 'Station 3', 'Station 4', 'Station 5',
            'Station 6', 'Station 7', 'Station 8', 'Station 9', 'Station 10']
G.add_nodes_from(stations)

# Define connections between some stations
connections = [('Station 1', 'Station 2'), ('Station 2', 'Station 3'), 
               ('Station 3', 'Station 4'), ('Station 4', 'Station 5'), 
               ('Station 5', 'Station 6'), ('Station 6', 'Station 7'), 
               ('Station 7', 'Station 8'), ('Station 8', 'Station 9'), 
               ('Station 9', 'Station 10'), ('Station 1', 'Station 5'), 
               ('Station 2', 'Station 8'), ('Station 3', 'Station 9'), 
               ('Station 4', 'Station 10')]

# Add the connections to the graph
G.add_edges_from(connections)

# Visualize the graph
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='lightblue', node_size=2000, font_size=12, font_weight='bold', pos=nx.spring_layout(G))
plt.title("Metro Station Network")
plt.show()

# Output basic characteristics of the graph
print("Number of stations:", G.number_of_nodes())
print("Number of connections between stations:", G.number_of_edges())
print("Degree of each station:")
for station, degree in G.degree():
    print(f"{station}: {degree}")
