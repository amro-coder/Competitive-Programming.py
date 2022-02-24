# There are three friend living on the straight line Ox in Lineland.
# The first friend lives at the point x1, the second friend lives at the point x2, and the third friend lives at the point x3.
# They plan to celebrate the New Year together, so they need to meet at one point.
# What is the minimum total distance they have to travel in order to meet at some point and celebrate the New Year?
#
# It's guaranteed that the optimal answer is always integer.

x=list(map(int,input().split()))
print(max(x)-min(x))