def getWeightedGraph(n):
  graph = {}
  for i in range(n):
    x , y , w = input().split()
    x = int(x)
    y = int(y)
    w = int(w)
    ll = graph.get(x)
    if ll is None:
      ll = []
    ll.append((y,w))
    graph[x]= ll
  return graph
def minimum(lst):
  min = lst[0][1]
  idx = 0
  for i in range(len(lst)):
    if lst[i][1]<min:
      min = lst[i][1]
      idx = i
  return idx
def getHeuristic(n):
  lst = {}
  print("Enter Heuristics (x --> h) :")
  for i in range(1,n):
    h = int(input("H for " + str(i) + ":"))
    lst[i]=h
  return lst
def Dijkstra(G,n,start_node,Heuristics):
  infinity= 9999999999
  visited = []
  queue = []
  D = {}
  previous = {}
  for i in range(n+1):
    D[i]=infinity
    previous[i]= None
  queue.append((start_node,0))
  D[start_node]=0
  while queue:
    x = queue.pop(minimum(queue))
    visited.append(x[0])
    nodes = G.get(x[0])
    if nodes is not None:
      for node in nodes :
        if node[0] not in visited:
          tmp = D[x[0]] + node[1] + Heuristics[node[0]]
          if tmp < D[node[0]]:
            D[node[0]]= tmp
            previous[node[0]]=x[0]
          queue.append(node)
  return visited,D
n = int(input("Enter the number of edges:"))
graph = getWeightedGraph(n)
Heuristics = getHeuristic(n)
print(graph)
print(Heuristics)
start_node = 1
visited,Dist = Dijkstra(graph,n,start_node,Heuristics)
for i in Dist:
  if i == 0 or Dist[i]==9999999999:
    continue
  print('Distance of node '+ str(i) + ' from ' + str(start_node) + ' is '+ str(Dist[i]))