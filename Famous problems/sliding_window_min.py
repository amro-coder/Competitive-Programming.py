from collections import deque
x=tuple(map(int,input().split()))
n=len(x)
window_size =int(input())
queue=deque()
i=0
while (i<window_size-1):
    if(not queue or (queue[-1][0]<x[i])):
        queue.append((x[i],i))
        i+=1
    else:
        queue.pop()
i=0
while (i+window_size<=n):
    if(queue and (queue[0][1]<i)):
        queue.popleft()
    current_element=i+window_size-1
    if(not queue or (queue[-1][0]<x[current_element])):
        queue.append((x[current_element],current_element))
        print(queue[0][0])
        i+=1
    else:
        queue.pop()






