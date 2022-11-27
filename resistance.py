import networkx as nx
import matplotlib.pyplot as plt
import scipy
G = nx.Graph()

G.add_node('Hamburg', pos=(0, 1))
G.add_node('Berlin', pos=(0,0))
G.add_node('Kota', pos = (0,3))

G.add_edge('Hamburg', 'Berlin',weight = 10)
G.add_edge('Berlin','Kota',weight=20)
nx.draw(G, nx.get_node_attributes(G, 'pos'), node_size=10)
print(G.edges(data=True))
print(nx.resistance_distance(G, 'Hamburg', 'Kota',weight='weight'))
plt.show()