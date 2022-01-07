# problem Statement:
# Given two strings, find the longest subsequence common both of them.
# This problem differs from problems of finding common substrings:
# unlike substrings, subsequences are not required to occupy consecutive positions within the original sequences

# solution:
string1=list(input())
string2=list(input())
dp=[[0]*(len(string2)+1) for _ in range(len(string1)+1)]
for i in range(len(string1)-1,-1,-1):
    for j in range(len(string2)-1,-1,-1):
        if(string1[i]!=string2[j]):
            dp[i][j]=max(dp[i+1][j],dp[i][j+1])
        else:
            dp[i][j]=dp[i+1][j+1]+1
# constructing the solution
ans=[]
i=j=0
while(len(ans)<dp[0][0]):
    if(dp[i][j]==dp[i+1][j]):
        i+=1
    elif(dp[i][j]==dp[i][j+1]):
        j+=1
    else:
        ans.append(string1[i])
        i+=1
        j+=1
print(dp[0][0])
print(''.join(ans))
