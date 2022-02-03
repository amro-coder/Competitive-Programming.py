from collections import defaultdict
def customFunction():
    return "no bigger element for this element"
def getNextBigger(x):
    stack = []
    ans = defaultdict(customFunction)
    i = 0
    while (i < len(x)):
        if (not stack):
            stack.append(x[i])
            i += 1
        else:
            if (x[i] > stack[-1]):
                ans[stack.pop()] = x[i]
            else:
                stack.append(x[i])
                i += 1
    return ans
x=tuple(map(int,input().split()))
ans=getNextBigger(x)
for i in x:
    print(i,ans[i])

