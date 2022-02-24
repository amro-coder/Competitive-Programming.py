# ou are given two arrays a and b both consisting of n positive (greater than zero) integers.
#  You are also given an integer k.
# In one move, you can choose two indices i and j (1≤i,j≤n) and swap ai and bj (i.e.ai becomes bj and vice versa).
#  Note that i and j can be equal or different (in particular, swap a2 with b2 or swap a3 and b9 both are acceptable moves).
# Your task is to find the maximum possible sum you can obtain in the array a if you can do no more than (i.e.at most) k such moves (swaps).
# You have to answer t independent test cases.
#
#
#
#  solution:

for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    b.sort(reverse=True)
    ans=sum(a)
    for i in range(k):
        ans+=max(0,b[i]-a[i])
    print(ans)