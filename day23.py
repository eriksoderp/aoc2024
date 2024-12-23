import networkx as nx
from networkx.algorithms.clique import enumerate_all_cliques
connections = open('input23.txt').read().strip().split('\n')

G = nx.Graph()
list(G.add_edge(*connection.split('-')) for connection in connections)
all_cliques = list(enumerate_all_cliques(G))
cliques = [c for c in all_cliques if len(c) == 3 and any(n[0] == 't' for n in c)]

print(len(cliques)) # Part 1
print(','.join(sorted(all_cliques[-1]))) # Part 2
