# index starts from one
# let xi be the nearst power of two that can divide the index i
# each element in the fenwick tree in index i has the sum of range of xi elements that end in index i
def get_sum(index,fenwick_tree):
    ans=0
    while(index>0):
        ans+=fenwick_tree[index]
        index-=(index)&(-index)
    return ans
def update_tree(index,value,fenwick_tree):
    while(index<len(fenwick_tree)):
        fenwick_tree[index]+=value
        index+=(index)&(-index)
    return
def constuct_fenwick_tree(array):
    n=(len(array))
    fenwick_tree=[0]*n
    for i in range(1,n):
        update_tree(i,array[i],fenwick_tree)
    return fenwick_tree
# index start from one
# get_sum(index) returns the sum including x
def get_range_sum(a,b):
    # a and b are included
    return get_sum(b,fenwick_tree)-get_sum(a-1,fenwick_tree)

# remmber to add the 0 to x
x=[0]+list(map(int,input().split()))
fenwick_tree=constuct_fenwick_tree(x)
print(get_range_sum(2,5))
update_tree(3,10-x[3],fenwick_tree)
print(get_range_sum(2,5))

