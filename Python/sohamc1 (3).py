class Graph:
    def __init__(self, vertices, flag = False):
        self.V = vertices  # No. of vertices
        self.graph = {}  # default dictionary to store graph
        if flag == True:
            for i in range(vertices+1):
                self.graph[i] = []
        else:
            for i in range(vertices):
                self.graph[i] = []

        self.scclist = []
        self.Time = 0

    def adjsort(self):
        for i in range(self.V):
            self.graph[i] = sorted(self.graph[i])

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function used by DFS
    def DFSUtil(self, v, visited, scc):
        # Mark the current node as visited and print it
        visited[v] = True
        scc.append(v)
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited, scc)
        return scc

    def fillOrder(self, v, visited, stack):
        # Mark the current node as visited
        visited[v] = True
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.fillOrder(i, visited, stack)
        stack = stack.append(v)

    # Function that returns reverse (or transpose) of this graph

    def getTranspose(self):
        g = Graph(self.V)

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)
        return g

    # The main function that finds and prints all strongly
    #       connected components

    def createSCCs(self):

        stack = []
        # Mark all the vertices as not visited (For first DFS)
        visited = [False]*(self.V)
        # Fill vertices in stack according to their finishing
        # times
        for i in range(self.V):
            if visited[i] == False:
                self.fillOrder(i, visited, stack)

        # Create a reversed graph
        gr = self.getTranspose()

        # Mark all the vertices as not visited (For second DFS)
        visited = [False]*(self.V)

        # Now process all vertices in order defined by Stack
        while stack:
            i = stack.pop()
            if visited[i] == False:
                scc = gr.DFSUtil(i, visited, [])
                self.scclist.append(scc)

    # A recursive function used by topologicalSort
    def topologicalSortUtil(self, v, visited, stack):

        # Mark the current node as visited.
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        # Push current vertex to stack which stores result
        stack.append(v)

    # The function to do Topological Sort. It uses recursive
    #       topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False]*self.V
        stack = []

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        # return contents of the stack
        return stack[::-1]  # return list in reverse order

 
        


v, e = list(map(int, input().split()))
vval = list(map(int, input().split()))
minvertex = v
g = Graph(v, True)
for i in range(e):
    v1, v2 = list(map(int, input().split()))
    if min(v1,v2) < minvertex:
        minvertex = min(v1,v2)
    if v1 == v2:
        pass
    else:
        g.addEdge(v1, v2)
if minvertex == 1:
    gg = Graph(v)
    for i in g.graph:
        for j in g.graph[i]:
            gg.addEdge(i-1,j-1)
    g = gg


start = int(input())
if minvertex == 1:
    start = start -1

g.createSCCs() 

sccval = []
scclen = len(g.scclist)
# this array b keeps the index of scc for each vertex
b = [-1 for _ in range(v)]
for scc in range(scclen):
    sum = 0
    for i in g.scclist[scc]:
        sum += vval[i]
        b[i] = scc
    sccval.append(sum)
u = b[start]

# creating a new dag graph with each scc as vertex
X = Graph(scclen)
# i th scc
for i in range(scclen):
    # j th vertex i th scc
    for j in g.scclist[i]:
        # k th neighbour of j th vertex in i th scc
        for k in g.graph[j]:
            # checks if the neighbour isnt in same scc
            if i != b[k]:
                # if not then i th scc is connected to scc index of k th neighbour
                X.addEdge(i, b[k])


Y = X.getTranspose()


# in dag scc graph we take maxpath value upto i from u
#       maxfrom path value upto parent of i's from u
toposort = X.topologicalSort()
k = 0
while toposort[k] != u:
    k += 1
maxto = [-1 for _ in range(scclen)]
maxto[u] = sccval[u]
# for any index in maxto it keeps the maxpath value to go from u
for i in range(k, scclen):
    if maxto[toposort[i]] == -1:
        continue
    for j in X.graph[toposort[i]]:
        if maxto[j] == -1:
            maxto[j] = sccval[j]
        maxto[j] = max(maxto[j], maxto[toposort[i]]+sccval[j])
maxfrom = [-1 for _ in range(scclen)]
maxfrom[u] = sccval[u]
for i in range(k, -1):
    if maxfrom[toposort[i]] == -1:
        continue
    for j in Y.graph[toposort[i]]:
        if maxfrom[j] == -1:
            maxfrom[j] = sccval[j]
        maxfrom[j] = max(maxfrom[j], maxfrom[toposort[i]]+sccval[j])
finalsum=0
maxx=0
for i in range(scclen):
    mx1 = mx2 = 0
    if i == u:
        continue
    if maxfrom[i] != -1:
        for j in X.graph[i]:
            if maxfrom[i] >= 0 and maxto[j] >= 0:
                mx1 = max(mx1, maxfrom[i] + maxto[j] - sccval[u])
    if maxto[i] != -1:
        for j in Y.graph[i]:
            if maxto[i] >= 0 and maxfrom[j] >= 0:
                mx2 = max(mx2, maxto[i] + maxfrom[j] - sccval[u])
    maxx = max(maxx, mx1, mx2)
finalsum = max(maxx, finalsum)
if finalsum == 0: finalsum = max(finalsum, sccval[u])
print(finalsum)