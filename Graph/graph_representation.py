# 1-adjecency list using dictioneries
from collections import defaultdict
graph = defaultdict(list)
def addEdgeUniDirectionWithLength(graph,start,end,length):
    graph[start].append((end,length))

def addEdgeBothDirectionsWithLength(graph,start,end,length):
    # going path
    graph[start].append((end,length))
    # returning path
    graph[end].append((start,length))

def addEdgeUniDirections(graph,start,end):
    graph[start].append(end)

def addEdgeBothDirections(graph,start,end):
    # going path
    graph[start].append(end)
    # returning path
    graph[end].append(start)
def initalizeNodes(graph,value):
    nodes={}
    for parent,children in graph.items():
        for child in children:
             nodes[parent]=value
             # cause if the edge have a length it will be in form of tuples
             try:
                nodes[child[0]]=value
             except:
                 nodes[child] = value
    return nodes

def getPath(parents,node):
    ans=[]
    while(True):
        if(parents[node]==None):
            ans.append(node)
            break
        ans.append(parents[node])
        node=parents[node]
    ans.reverse()
    return ans

# def getEdges(graph):
#     edges=[]
#     for start in graph.keys():
#         for dest in
# 2-
