# This is an interactive problem.
#
# We picked an array of whole numbers a1,a2,…,an (0≤ai≤109) and concealed exactly one zero in it!
#  Your goal is to find the location of this zero, that is, to find i such that ai=0.
#
# You are allowed to make several queries to guess the answer.
#  For each query, you can think up three distinct indices i,j,k, and we will tell you the value of max(ai,aj,ak)−min(ai,aj,ak).
#  In other words, we will tell you the difference between the maximum and the minimum number among ai, aj and ak.
#
# You are allowed to make no more than 2⋅n−2 queries, and after that you have two tries to guess where the zero is.
#  That is, you have to tell us two numbers i and j and you win if ai=0 or aj=0.
#
# Can you guess where we hid the zero?
#
# Note that the array in each test case is fixed beforehand and will not change during the game.
# In other words, the interactor is not adaptive.

# solution:
def ask(i,j,k):
    print("?",i,j,k,flush=True)
    return int(input())
def print_ans(i,j):
    print("!", i, j,flush=True)
    return
def min_max(a,b,c,d):
    a1=ask(a,b,c)
    a2=ask(a,b,d)
    a3=ask(a,c,d)
    a4=ask(b,c,d)
    if(a1==a2 and a1>=a3 and a1>=a4):
        return a,b
    elif (a1 == a3 and a1 >= a2 and a1 >= a4):
        return a,c
    elif (a2 == a3 and a2 >= a1 and a2 >= a4):
        return a, d
    elif (a1 == a4 and a1 >= a2 and a1 >= a3):
        return b, c
    elif (a2 == a4 and a2 >= a3 and a2 >= a1):
        return b, d
    else:
        return c,d

for _ in range(int(input())):
    n=int(input())
    a,b=min_max(1,2,3,4)
    if(a!=1 and b!=1):
        dont_care=1
    elif (a != 2 and b != 2):
        dont_care = 2
    else:
        dont_care=3
    for i in range(5,n+1,2):
        if(i+1<=n):
            a,b=min_max(a,b,i,i+1)
        else:
            a, b = min_max(a, b, i,dont_care)
    print_ans(a,b)

