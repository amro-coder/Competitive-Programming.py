#problem
# Did you know you can download more RAM? There is a shop with n different pieces of software that increase your RAM.
# The i-th RAM increasing software takes ai GB of memory to run (temporarily, once the program is done running, you get the RAM back),
# and gives you an additional bi GB of RAM (permanently). Each software can only be used once. Your PC currently has k GB of RAM.
# Note that you can't use a RAM-increasing software if it takes more GB of RAM to use than what you currently have.
# Since RAM is the most important thing in the world, you wonder, what is the maximum possible amount of RAM achievable?

#solution:
import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b = list(map(int, input().split()))
    a_b=[]
    for i in range(n):
        a_b.append((a[i],b[i]))
    a_b.sort()
    for i in range(n):
        if(a_b[i][0]>k):
            break
        else:
            k+=a_b[i][1]
    print(k)