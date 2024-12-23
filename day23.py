import networkx as nx
from networkx.algorithms.clique import enumerate_all_cliques
connections = open('input23.txt').read().strip().split('\n')

G = nx.Graph()
list(G.add_edge(*connection.split('-')) for connection in connections)
all_cliques = list(enumerate_all_cliques(G))
cliques = [c for c in all_cliques if len(c) == 3 and any(n[0] == 't' for n in c)]

print(len(cliques)) # Part 1
print(','.join(sorted(all_cliques[-1]))) # Part 2

# Own implementation instead of using networkx (except the graph structure)
# Part 1
cliques = set()
for a in G.nodes():
    for b in G[a]:
        for c in G[b]:
            if a in G[c]:
                if any(n[0] == 't' for n in [a, b, c]):
                    cliques.add(tuple(sorted([a, b, c])))

print(len(cliques))

# Part 2
maximal_cliques = []
def bron_kerbosch(R, P, X):
    if not P and not X:
        return maximal_cliques.append(R)
    while P:
        v = P.pop()
        bron_kerbosch(R.union([v]), P.intersection(G[v]), X.intersection(G[v]))
        X.add(v)

R, P, X = set(), set(G.nodes()), set()
bron_kerbosch(R, P, X)
print(','.join(sorted(max(maximal_cliques, key=len))))
