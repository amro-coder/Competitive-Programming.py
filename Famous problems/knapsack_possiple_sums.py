def all_possiple_sums():
    dp = [False] * (max_value + 1)
    dp[0] = True
    for i in range(n):
        for j in range(max_value, value[i] - 1, -1):
            dp[j] |= dp[j - value[i]]
    ans=[]
    for i in range(max_value + 1):
        if (dp[i]):
            ans.append(i)
    return ans

def number_of_occurrences():
    dp = [0] * (max_value + 1)
    dp[0] = 1
    for i in range(n):
        for j in range(max_value, value[i] - 1, -1):
            dp[j] += dp[j - value[i]]
    return dp

n=int(input())
value=tuple(map(int,input().split()))
max_value=sum(value)
print(*all_possiple_sums())
print(*number_of_occurrences())

