# problem statement
#Rahul and Tina are looking forward to starting their new year at college. As they enter their new classroom, they observe the seats of students are arranged in a n×m grid.
# The seat in row r and column c is denoted by (r,c), and the distance between two seats (a,b) and (c,d) is |a−c|+|b−d|.
# As the class president, Tina has access to exactly k buckets of pink paint. The following process occurs.
# First, Tina chooses exactly k seats in the classroom to paint with pink paint.
# One bucket of paint can paint exactly one seat.
# After Tina has painted k seats in the previous step, Rahul chooses where he sits.
# He will not choose a seat that has been painted pink due to his hatred of the colour pink.
# After Rahul has chosen his seat, Tina chooses a seat for herself.
# She can choose any of the seats, painted or not, other than the one chosen by Rahul.
# Rahul wants to choose a seat such that he sits as close to Tina as possible.
# However, Tina wants to sit as far away from Rahul as possible due to some complicated relationship history that we couldn't fit into the statement!
# Now, Rahul wonders for k=0,1,…,n⋅m−1, if Tina has k buckets of paint, how close can Rahul sit to Tina,
# if both Rahul and Tina are aware of each other's intentions and they both act as strategically as possible?
# Please help satisfy Rahul's curiosity!
# solution
import sys
input=sys.stdin.readline
for _ in range(int(input())):
    n,m=map(int,input().split())
    start=(n//2)+(m//2)
    ans=[]
    row=[]
    col=[]
    if(n%2!=0):
        row.append(1)
        n-=1
    for _ in range(n//2):
        row.append(2)

    if (m % 2 != 0):
        col.append(1)
        m -= 1
    for _ in range(m//2):
        col.append(2)

    for i in range(len(row)):
        for j in range(len(col)):
            for _ in range(row[i]):
                for __ in range(col[j]):
                    ans.append(start + i + j)
    ans.sort()
    print(*ans)

