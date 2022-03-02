# There are n beautiful skyscrapers in New York, the height of the i-th one is hi.
# Today some villains have set on fire first n−1 of them, and now the only safety building is n-th skyscraper.
#
# Let's call a jump from i-th skyscraper to j-th (i<j) discrete, if all skyscrapers between are strictly lower or higher than both of them.
# Formally, jump is discrete, if i<j and one of the following conditions satisfied:
# i+1=j
# max(hi+1,…,hj−1)<min(hi,hj)
# max(hi,hj)<min(hi+1,…,hj−1).
# At the moment, Vasya is staying on the first skyscraper and wants to live a little longer, so his goal is to reach n-th skyscraper with minimal count of discrete jumps.
# Help him with calcualting this number.

# solution:
from collections import deque
def BFS(start):
    q=deque([start])
    visited[start]=True
    distances[start]=0
    while q:
        parent=q.popleft()
        for child in graph[parent]:
            if (not visited[child]):
                visited[child]=True
                q.append(child)
                distances[child]=distances[parent]+1
    return
import sys
input=sys.stdin.readline
n=int(input())
x=list(map(int,input().split()))
graph=[set() for _ in range(n)]
stack=[]
for sign in range(2):
    for i in range(n):
        while (stack and x[i] > x[stack[-1]]):
                graph[stack.pop()].add(i)
        if (stack):
            graph[stack[-1]].add(i)
            if(x[stack[-1]]==x[i]):
                stack.pop()
        stack.append(i)
    for i in range(n):
        x[i]=-x[i]

visited=[False]*(n)
distances=[-1]*(n)
BFS(0)
print(distances[n-1])