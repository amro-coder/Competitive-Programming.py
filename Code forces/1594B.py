# Theofanis really likes sequences of positive integers,
# thus his teacher (Yeltsa Kcir) gave him a problem about a sequence that consists of only special numbers.
#
# Let's call a positive number special if it can be written as a sum of different non-negative powers of n.
# For example, for n=4 number 17 is special, because it can be written as 40+42=1+16=17, but 9 is not.
#
# Theofanis asks you to help him find the k-th special number if they are sorted in increasing order.
# Since this number may be too large, output it modulo 109+7.

# solution:
mod=(10**9)+7
for _ in range(int(input())):
    n,k=map(int,input().split())
    ans=i=0
    while(k):
        if(k&1):
            ans+=pow(n,i,mod)
        i+=1
        k>>=1
        ans%=mod
    print(ans%mod)