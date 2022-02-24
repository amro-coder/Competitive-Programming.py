# Among Johnny's numerous hobbies, there are two seemingly harmless ones: applying bitwise operations and sneaking into his dad's office.
# As it is usually the case with small children, Johnny is unaware that combining these two activities can get him in a lot of trouble.
#
# There is a set S containing very important numbers on his dad's desk.
# The minute Johnny heard about it, he decided that it's a good idea to choose a positive integer k and replace each element s of the set S with s⊕k (⊕ denotes the exclusive or operation).
#
# Help him choose such k that Johnny's dad will not see any difference after his son is done playing (i.e. Johnny will get the same set as before playing).
# It is possible that no such number exists. It is also possible that there are many of them.
# In such a case, output the smallest one. Note that the order of elements in a set doesn't matter, i.e. set {1,2,3} equals to set {2,1,3}.
#
# Formally, find the smallest positive integer k such that {s⊕k|s∈S}=S or report that there is no such number.
#
# For example, if S={1,3,4} and k=2, new set will be equal to {3,1,6}. If S={0,1,2,3} and k=1, after playing set will stay the same.


# solution:
for _ in range(int(input())):
    n=int(input())
    x=list(map(int,input().split()))
    for k in range(1,1<<11):
        y=x.copy()
        for i in x:
            y.append(i^k)
        y.sort()
        for i in range(0,2*n,2):
            if(y[i]^y[i+1]!=0):
                break
        else:
            print(k)
            break
    else:
        print(-1)