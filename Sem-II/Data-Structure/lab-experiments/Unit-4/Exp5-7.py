table_size = 5
table = [[] for _ in range(table_size)]

def h(k):
    return k % table_size

def insert(k, v):
    i = h(k)
    for j in range(len(table[i])):
        if table[i][j][0] == k:
            table[i][j] = (k, v)
            return
    table[i].append((k, v))

def get(k):
    i = h(k)
    for key, val in table[i]:
        if key == k:
            return val
    return None

def delete(k):
    i = h(k)
    for j in range(len(table[i])):
        if table[i][j][0] == k:
            table[i].pop(j)
            return True
    return False

n = int(input())
for _ in range(n):
    k, v = map(int, input().split())
    insert(k, v)

for i in range(table_size):
    print(i, "->", table[i])

q = int(input())
for _ in range(q):
    t, k = input().split()
    k = int(k)
    if t == "get":
        print(get(k))
    elif t == "del":
        print(delete(k))

for i in range(table_size):
    print(i, "->", table[i])