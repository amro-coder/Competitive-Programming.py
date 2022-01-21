import sys
input=sys.stdin.readline
x=tuple(map(int,input().strip().split()))
currentSum=0
maxSum=0
for i in range(len(x)):
    currentSum+=x[i]
    maxSum=max(maxSum,currentSum)
    currentSum=max(0,currentSum)
print(maxSum)