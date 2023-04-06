from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # No. of vertices
        self.graph =  defaultdict(list) # default dictionary to store graph

        self.scclist = []

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
        visited = [False]*(self.V+1)
        # Fill vertices in stack according to their finishing
        # times
        for i in range(self.V):
            if visited[i] == False:
                self.fillOrder(i, visited, stack)

        # Create a reversed graph
        gr = self.getTranspose()

        # Mark all the vertices as not visited (For second DFS)
        visited = [False]*(self.V+1)

        # Now process all vertices in order defined by Stack
        while stack:
            i = stack.pop()
            if visited[i] == False:
                scc = gr.DFSUtil(i, visited, [])
                self.scclist.append(scc)


    def topologicalSort(self):
        Q=[]
        S=[]
        indeg=[0]*(self.V+1)
        indeg[0]="useless"
        
        for i in self.graph:
            for j in self.graph[i]:
                
                indeg[j]+=1
        for i in range(0,self.V+1):
            if indeg[i]=="useless" or indeg[i]>0:
                pass
            else:
                Q.append(i)
                S.append(i)
                
        while Q:
            j=Q[0]
            del Q[0]
            for k in self.graph[j]:
                indeg[k]-=1
                if indeg[k]==0:
                    Q.append(k)
                    S.append(k)
        return S

 
        


v, e = list(map(int, input().split()))
vval = list(map(int, input().split()))
vval = ["useless"] + vval

g = Graph(v+1)
dict={}
for i in range(1,v+1): 
    dict[i]=[]

for i in range(e):
    v1, v2 = list(map(int, input().split()))
    if v1 == v2:
        pass
    else:
        g.addEdge(v1, v2)
        dict[v1].append(v2)
    


start = int(input())

g.createSCCs() 

# removes [0]--connected component from SCC list as it is not useful
for i in g.scclist:
    if i == [0]:
        g.scclist.remove([0])
    else:
        pass
scclen = len(g.scclist)
sccval = ["useless"] + [0]*scclen
# this array b keeps the index of scc for each vertex
b = [-1 for _ in range(g.V+1)]
for i in g.scclist:
    for j in i:
        b[j] = g.scclist.index(i)+1
b[0] = "useless"
u = b[start]

# creating a new dag graph with each scc as vertex
Xdict={}
for i in range(1, scclen+1):
    Xdict[i] = []
# i th vertex in dict
for i in dict:
    # j th neighbour i th vertex
    for j in dict[i]:
            if b[i] != b[j]:
                # if not then i th scc is connected to scc index of k th neighbour
                if b[j] in Xdict[b[i]]:
                    pass
                else:
                    Xdict[b[i]].append([b[j]])
    sccval[b[i]] += vval[i]


X = Graph(scclen)
for i in Xdict:
    for j in Xdict[i]:
        X.addEdge(i,j[0])

Y = X.getTranspose()


# in dag scc graph we take maxpath value upto i from u
#       maxfrom path value upto parent of i's from u
toposort = X.topologicalSort()
toposort = ["useless"] + toposort

# Find the starting scc in toposort
k = toposort.index(u)
maxto = ["useless"] + [-1 for _ in range(scclen)]
maxto[u] = sccval[u]
# for any index in maxto it keeps the maxpath value to go from u
for i in range(k, scclen+1):
    if maxto[toposort[i]] == -1:
        continue
    for j in X.graph[toposort[i]]:
        if maxto[j] == -1:
            maxto[j] = sccval[j]
        maxto[j] = max(maxto[j], maxto[toposort[i]]+sccval[j])

print(scclen)
maxfrom = ["useless"] + [-1 for _ in range(scclen)]
maxfrom[u] = sccval[u]
for i in range(k,0, -1):
    if maxfrom[toposort[i]] == -1:
        continue
    for j in Y.graph[toposort[i]]:
        if maxfrom[j] == -1:
            maxfrom[j] = sccval[j]
        maxfrom[j] = max(maxfrom[j], maxfrom[toposort[i]]+sccval[j])
finalsum = sccval[u]
maxx=0
for i in range(1,scclen+1):
    mx1 = 0
    if i == u:
        continue

    if maxto[i] != -1:
        for j in Y.graph[i]:
            if maxto[i] >= 0 and maxfrom[j] >= 0:
                mx1 = max(mx1, maxto[i] + maxfrom[j] - sccval[u])
    finalsum = max(mx1, finalsum)

print(finalsum)