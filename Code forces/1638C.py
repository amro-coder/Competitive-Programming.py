# You are given a permutation p1,p2,…,pn.
# Then, an undirected graph is constructed in the following way: add an edge between vertices i, j such that i<j if and only if pi>pj.
# Your task is to count the number of connected components in this graph.
#
# Two vertices u and v belong to the same connected component if and only if there is at least one path along edges connecting u and v.
#
# A permutation is an array consisting of n distinct integers from 1 to n in arbitrary order.

# For example, [2,3,1,5,4] is a permutation, but [1,2,2] is not a permutation (2 appears twice in the array) and [1,3,4] is also not a permutation (n=3 but there is 4 in the array).

import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    index=[-1]*(n+1)
    visited=[False]*n
    for i in range(n):
        index[x[i]]=i
    ans=0
    min_visited=float("inf")
    for i in range(n,0,-1):
        if(not visited[index[i]]):
            if(i<min_visited):
                ans+=1
            for j in range(index[i],n):
                min_visited=min(min_visited,x[j])
                if(visited[j]):
                    break
                else:
                    visited[j]=True
    print(ans)

