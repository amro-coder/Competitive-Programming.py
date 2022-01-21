# problem Statement:
# Suppose we have two words made up from some letters, such as
# V = T G A T G G A T C
# W = G T T T G C A C
# We want to find the longest contiguous sequence of letters (subword) that is contained in both words.
# In this case, the longest common subword is "T G"

# Solution:
string1=list(input())
string2=list(input())
# bruteForce for fun (:
# ans=0
# string=""
# for i in range(len(string1)):
#     for j in range(i,len(string1)):
#         for k in range(len(string2)):
#             for l in range(k,len(string2)):
#                 if(string1[i:j+1]==string2[k:l+1]):
#                     if(j+1-i>ans):
#                         ans=j+1-i
#                         string=string1[i:j+1]
# print(ans)
# print(string)
# now lets dp
ans=float('-inf')
index=-1
dp=[[0]* (len(string2)+1) for _ in range(len(string1)+1)]
for i in range(len(string1)-1,-1,-1):
    for j in range(len(string2)-1,-1,-1):
        if(string1[i]!=string2[j]):
            dp[i][j] = 0
        else:
            dp[i][j]=dp[i+1][j+1]+1
        if(dp[i][j]>ans):
            ans=dp[i][j]
            index=i
print(ans)
print(' '.join(string1[i:i+ans]))