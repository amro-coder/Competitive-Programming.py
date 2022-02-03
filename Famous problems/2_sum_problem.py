def dosetargetExisit(target, x):
    i = 0
    j = len(x) - 1
    while (i < j):
        if (x[i] + x[j] == target):
            return [True, (x[i], x[j])]
        if (x[i] + x[j] > target):
            j -= 1
        else:
            i += 1
    return [False]


x = list(map(int, input().split()))
target = int(input())
x.sort()
ans = dosetargetExisit(target, x)
if (ans[0]):
    print(f"found sum using {ans[1][0]} + {ans[1][1]}")
else:
    print("sum not found")
# 3Sum can be solved in o(n^2) with the same approach
