# Petr has just bought a new car. He's just arrived at the most known Petersburg's petrol station to refuel it when he suddenly discovered that the petrol tank is secured with a combination lock!
# The lock has a scale of 360 degrees and a pointer which initially points at zero:
# Petr called his car dealer, who instructed him to rotate the lock's wheel exactly n times.
# The i-th rotation should be ai degrees, either clockwise or counterclockwise,
# and after all n rotations the pointer should again point at zero.

# This confused Petr a little bit as he isn't sure which rotations should be done clockwise and which should be done counterclockwise.
# As there are many possible ways of rotating the lock, help him and find out whether there exists at least one,
# such that after all n rotations the pointer will point at zero again.
n=int(input())
x=[int(input()) for _ in range(n)]
for i in range(1<<n):
    sum=0
    for j in range(n):
        if((i>>j)&1):
            sum+=x[j]
        else:
            sum-=x[j]
    if(sum%360==0):
        print("yes")
        break
else:
    print("NO")