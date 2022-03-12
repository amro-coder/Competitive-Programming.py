def prime_factors(x):
    ans=[]
    while not x&1:
        ans.append(2)
        x=x//2
    for i in range(3,int(x**0.5+2),2):
        while x%i==0:
            ans.append(i)
            x//=i
    if x>2:
        ans.append(x)
    return ans
print(*prime_factors(int(input())))


