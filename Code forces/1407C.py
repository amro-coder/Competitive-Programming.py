# This is an interactive problem.
#
# We hid from you a permutation p of length n, consisting of the elements from 1 to n. You want to guess it.
# To do that, you can give us 2 different indices i and j, and we will reply with pimodpj (remainder of division pi by pj).
#
# We have enough patience to answer at most 2⋅n queries, so you should fit in this constraint. Can you do it?
#
# As a reminder, a permutation of length n is an array consisting of n distinct integers from 1 to n in arbitrary order.
# For example, [2,3,1,5,4] is a permutation, but [1,2,2] is not a permutation (2 appears twice in the array) and [1,3,4] is also not a permutation (n=3 but there is 4 in the array).

# sloution:
def ask(i,j):
    print("?",i,j,flush=True)
    return int(input())
def print_ans(x):
    print("!",*x)
    exit()
n=int(input())
if(n==1):
    print_ans([1])
else:
    x=[0]*(n)
    last_biggest_index=1
    for i in range(2,n+1):
        a=ask(last_biggest_index,i)
        b=ask(i,last_biggest_index)
        if(a>b):
            x[last_biggest_index-1]=a
            last_biggest_index=i
        else:
            x[i-1]=b
    x[last_biggest_index-1]=n
    print_ans(x)

