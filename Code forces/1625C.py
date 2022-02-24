# The Government of Mars is not only interested in optimizing space flights, but also wants to improve the road system of the planet.
#
# One of the most important highways of Mars connects Olymp City and Kstolop, the capital of Cydonia.
# In this problem, we only consider the way from Kstolop to Olymp City, but not the reverse path (i. e. the path from Olymp City to Kstolop).
#
# The road from Kstolop to Olymp City is ℓ kilometers long. Each point of the road has a coordinate x (0≤x≤ℓ), which is equal to the distance from Kstolop in kilometers. So, Kstolop is located in the point with coordinate 0, and Olymp City is located in the point with coordinate ℓ.
#
# There are n signs along the road, i-th of which sets a speed limit ai.
# This limit means that the next kilometer must be passed in ai minutes and is active until you encounter the next along the road.
# There is a road sign at the start of the road (i. e. in the point with coordinate 0), which sets the initial speed limit.
#
# If you know the location of all the signs, it's not hard to calculate how much time it takes to drive from Kstolop to Olymp City.

# To optimize the road traffic, the Government of Mars decided to remove no more than k road signs.
# It cannot remove the sign at the start of the road, otherwise, there will be no limit at the start.
# By removing these signs, the Government also wants to make the time needed to drive from Kstolop to Olymp City as small as possible.

# The largest industrial enterprises are located in Cydonia, so it's the priority task to optimize the road traffic from Olymp City.
# So, the Government of Mars wants you to remove the signs in the way described above.

import sys
input=sys.stdin.readline
n,l,k=map(int,input().split())
x=list(map(int,input().split()))+[l]
speed_limit=list(map(int,input().split()))
dp=[[float("inf")]*(k+1) for _ in range(n+1)]
dp[0][0]=0
for i in range(1,n+1):
    for j in range(k+1):
        for l in range(max(0, i - 1 - j),i):
            dp[i][j] = min(dp[i][j], dp[l][j-(i-1-l)]+(speed_limit[l]*(x[i]-x[l])))
print(min(dp[n]))

