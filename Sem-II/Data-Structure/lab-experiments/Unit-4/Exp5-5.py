edges = [(1,2),(1,3),(2,3),(2,4),(3,5),(4,5),(4,6),(5,6),(6,1)]

adj = {}
for u, v in edges:
    if u not in adj:
        adj[u] = []
    if v not in adj:
        adj[v] = []
    adj[u].append(v)
    adj[v].append(u)

start = int(input())

visited = set([start])
q = [start]
res = []

while q:
    node = q.pop(0)
    res.append(node)
    for nei in adj.get(node, []):
        if nei not in visited:
            visited.add(nei)
            q.append(nei)

print(res)