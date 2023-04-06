from queue import Queue


def toposort(G, n):
    topo_sort = []
    Q = Queue(maxsize=n)
    indegree = [0]*(n+1)
    for v in range(n):
        for w in G[v]:
            indegree[w] += 1
    for v in range(n):
        if indegree[v] == 0:
            Q.put(v)
    while not Q.empty():
        v = Q.get()
        topo_sort.append(v)
        for w in G[v]:
            indegree[w] -= 1
            if indegree[w] == 0:
                Q.put(w)
    return (topo_sort)


# create scc through tarjan algo
def createscc(graph):
    result = []
    stack = []
    low = {}
    callstack = []
    for v in graph:
        callstack.append((v, 0, len(low)))
        while callstack:
            v, mark, num = callstack.pop()
            if mark == 0:
                if v in low:
                    continue
                low[v] = num
                stack.append(v)
            if mark > 0:
                low[v] = min(low[v], low[graph[v][mark-1]])
            if mark < len(graph[v]):
                callstack.append((v, mark+1, num))
                callstack.append((graph[v][mark], 0, len(low)))
                continue
            if num == low[v]:
                scc = []
                while True:
                    scc.append(stack.pop())
                    low[scc[-1]] = len(graph)
                    if scc[-1] == v:
                        break
                result.append(scc)
    return result


V, E = list(map(int, input().split()))  # Number of nodes and edges
vals = list(map(int, input().split()))  # List of values of each vertex
values = {}
for i in range(1, V+1):
    values[i] = vals[i-1]


g = {}
for i in range(1, V+1):
    g[i] = []

# Adding edges
for _ in range(E):
    start, end = list(map(int, input().split()))
    g[start] += [end]

st = int(input()) # Starting vertex
scclist = createscc(g)  # Create the scc list
sccindex = {}           # store the index of the scc in which i-th vertex is in
u = 0
for i in range(len(scclist)):  # print(scclist[i])
    for j in scclist[i]:
        sccindex[j] = i
        if j == st:
            u = i
val = [0 for _ in scclist]  # Stores values of nodes of each scc
for i in range(len(scclist)):
    for j in scclist[i]:
        val[i] += values[j]
X = [[] for _ in range(len(scclist))] # Creating Dag of scc nodes
for i in range(len(scclist)):
    for j in scclist[i]:
        for k in g[j]:
            if i != sccindex[k]:
                X[i].append(sccindex[k])
Xlen = len(X)  
# Array to store the maxpath value from i-th vertex to starting vertex
maxfrom = [-1 for _ in range(len(scclist))] 
# Array to store the maxpath value from starting vertex to i-th vertex
maxto = [-1 for _ in range(len(scclist))]
# Topological sort array
top = toposort(X, Xlen)


maxfrom[u] = maxto[u] = val[u]

# Y = X.transpose
Y = [[] for _ in range(Xlen)]
for i in range(Xlen):
    for j in X[i]:
        Y[j].append(i)
k = u
for i in range(Xlen):
    if u == top[i]:
        k = i

for i in range(k, Xlen):
    if maxto[top[i]] == -1:
        continue
    for j in X[top[i]]:
        if maxto[j] == -1:
            maxto[j] = val[j]  # if i==k:continue
        maxto[j] = max(maxto[top[i]]+val[j], maxto[j])
i = k
while i >= 0:
    if maxfrom[top[i]] == -1:
        i -= 1
        continue
    for j in Y[top[i]]:
        if maxfrom[j] == -1:
            maxfrom[j] = val[j]
        maxfrom[j] = max(maxfrom[top[i]]+val[j], maxfrom[j])
    i = i-1

# Final Answer
finalpathvalue = 0
maxx = 0
for i in range(0, Xlen):
    mx1 = mx2 = 0
    if i == u:
        continue
    if maxfrom[i] != -1:
        for j in X[i]:
            if(maxto[j] != -1 and maxfrom[i] != -1):
                m1 = maxfrom[i]+maxto[j]-val[u]
                mx1 = max(m1, mx1)
    if maxto[i] != -1:
        for j in Y[i]:
            if(maxfrom[j] != -1 and maxto[i] != -1):
                m2 = maxto[i]+maxfrom[j]-val[u]
                mx2 = max(m2, mx2)

    maxx = max(maxx, mx1, mx2)
finalpathvalue = max(maxx, finalpathvalue)
if finalpathvalue == 0:
    finalpathvalue = max(finalpathvalue, val[u])
print(finalpathvalue)
