edges = [(1,2),(1,3),(2,3),(2,4),(3,5),(4,5),(4,6),(5,6),(6,1)]

adj = {}

for u, v in edges:
    if u not in adj:
        adj[u] = []
    if v not in adj:
        adj[v] = []
    adj[u].append(v)
    adj[v].append(u)

for node in sorted(adj):
    print(str(node) + " -> " + " ".join(map(str, adj[node])))