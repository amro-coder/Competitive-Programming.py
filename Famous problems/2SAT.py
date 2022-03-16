# we have an equation that looks like:  (a1 ∨ b1)∧(a2 ∨ b2)∧··· ∧(am ∨ bm). Where v denotes logical or and ∧ denotes logical and.
# the a1,b1.... variables are either a logical variable or a negation of a logical variable.
# we want to know if we can assign a value to each variable so that the equation is true?
# let's define an implicit graph: an implicit graph is a graph with directed edges that means if a node is true then
# all nodes it can reach are true, but if it's false then there are no constrains.
# thus we can made an implicit graph by creating two directed edges for each clause of the form (a v b)
# edge 1 :  negate a to b : meaning that if a is false (negate a is true) then b must be true
# edge 2 :  negate b to a : meaning that if b is false (negate b is true) then a must be true
# note with this edges if a is false then b is ture and vice versa.
# notice edge 1 is contrapositive to edge 2, meaning we can not use both constrains , if we use edge 1 constrains then there are no constrains form edge 2 and vice versa.
# notice if we have a path form node a to node b then it's the same as an edge from a to b, because if a is true then the whole path is true.
# so now if we have a path from a to negate a and from negate a to a then if a is false the path from a to negate a will make a contradiction
# and if a is true then the path from a to negate a will make a contradiction, hence it's impossible to assign values so the equation is correct.
# now let's define strongly connected component(SCC): a SCC is a group of nodes such that each node can reach any node in the same SCC.
# now let's rephrase, after making the implicit graph , if any two nodes x and negate x are in the same strongly connected component then
# it's impossible to assign values to such equation.
# now if it's possible how do we assign the values?
# notice that a graph with it's SCCs  as it's nodes forms an acyclic graph which we can make a topological sorting to
# so if we start from the last SCC in the topological sorting , then we can assign the values easily
# since the component dose not leak to any other SCC, all we have to do is assign true to all nodes of the SCC
# and we keep going with this order till all variables are assigned values, notice that we don't change the value of a variable once we assign it.
# this way will guarantee that no edge is contradicted in the whole graph.
def dfs(start):
    working_stack=[start]
    while working_stack:
        parent=working_stack[-1]
        if visited[parent]==2:
            working_stack.pop()
            continue
        visited[parent]=1 # node is under processing
        finished=True
        for child in reversed_graph[parent]:
            if (visited[child]==0):
                finished=False
                working_stack.append(child)
        if finished:
            visited[parent]=2
            working_stack.pop()
            topo_sort.append(parent)

def dfs_visit(node):
    stack=[node]
    compenent=set()
    while stack:
        parent=stack.pop()
        if not visited[parent]:
            visited[parent]=True
            compenent.add(parent)
            for child in graph[parent]:
                if not visited[child]:
                    stack.append(child)
    return compenent
# the input should be of the form :
# n
# 1 2
# -1 2
# n represents the number of (a v b) clauses
# then n lines follow with 1 meaning variable 1 and -1 meaning the negate of variable 1 and so on.
# (a v b) ^ (¬a v b) ^ (c v ¬b)
# input for above equation is:
# 3
# 1 2
# -1 2
# 3 -2
from collections import defaultdict
n=int(input())
graph=defaultdict(list)
reversed_graph=defaultdict(list)
all_nodes=set()
for _ in range(n):
    a,b=map(int,input().split())
    all_nodes.add(a)
    all_nodes.add(-a)
    all_nodes.add(b)
    all_nodes.add(-b)
    graph[-a].append(b)
    graph[-b].append(a)
    reversed_graph[b].append(-a)
    reversed_graph[a].append(-b)
# constructing a node ordering from reversed graph
visited= dict.fromkeys(all_nodes,False)
topo_sort=[]
for node in all_nodes:
    if visited[node]==0:
        dfs(node)
topo_sort.reverse()
# using the order to process each connected component in the right order
visited= dict.fromkeys(all_nodes,False)
strongly_connected_components=[]
for node in topo_sort:
    if not visited[node]:
        strongly_connected_components.append(dfs_visit(node))
ans=[-1]*max(all_nodes)
out=False
for SCC in strongly_connected_components:
    for node in SCC:
        if -node in SCC:
            print("There is no way to assign values to variables so that the equation yields ture")
            out=True
            break
        if ans[abs(node)-1]==-1:
            ans[abs(node) - 1]= node>0
    if out:
        break
else:
    print("A solution exist and variables should be assigned as follows:")
    for i in range(len(ans)):
        print(f"the variable {i+1} should be {ans[i]}")

# Equation 1:
#  (x2 ∨ ¬x1)∧(¬x1 ∨ ¬x2)∧(x1 ∨ x3)∧(¬x2 ∨ ¬x3)∧(x1 ∨ x4)
# input form of equation 1:
# 5
# 2 -1
# -1 -2
# 1 3
# -2 -3
# 1 4
#
# Equation 2:
#   (x1 ∨ x2)∧(x1 ∨ ¬x2)∧(¬x1 ∨ x3)∧(¬x1 ∨ ¬x3)
# input form of equation 2:
# 4
# 1 2
# 1 -2
# -1 3
# -1 -3
