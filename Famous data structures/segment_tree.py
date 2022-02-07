# segment tree:
# implemented in an array of size (2*n)-1
# the size of the original array should be a power of two (you can always add elements that don't affect the result of the query)
# we construct it by making an array in which the two children of segment_tree[k] are segment_tree[k<<1] and segment_tree[k<<1 |1]
# and each parent have the value of the query to it's children
# note that we don't use index zero in the segment_tree
# odd index means that the element is the right child and even means it's the left child
# for the left border we include its element if it's a right child (if its left then the result of the query is stored in the parent)
# for the right border we include its element if it's a left child (if its right then the result of the query is stored in the parent)

# using segment_tree for prefix_sums
def constuct_segment_tree():
    segment_tree=[0]*(n<<1)
    for i in range(n):
        segment_tree[i+n]=array[i]
    for i in range(n-1,0,-1):
        segment_tree[i]=segment_tree[i<<1]+segment_tree[i<<1 |1]
    return segment_tree
def update_segment_tree(index,new_value):
    index += n
    segment_tree[index]=new_value
    while(index>0):
        segment_tree[index>>1]=segment_tree[index]+segment_tree[index^1]# xor left child with one = right child,xor right child with one = left child,
        index>>=1
    return
def get_range_sum(a,b):
    # both indexes are included in a range and indexing starts from zero
    a+=n
    b+=n
    ans=0
    while(a<=b):
        if(a & 1):#right child
            ans+=segment_tree[a]
            a+=1 # move right
        if(not (b & 1)):#left child
            ans+=segment_tree[b]
            b-=1
        a>>=1
        b>>=1

    return ans


array =list(map(int,input().split()))
n=len(array)
array.extend([0]*(2**((n-1).bit_length())-n)) # nearest power of two#
n=len(array)
segment_tree=constuct_segment_tree()
print(segment_tree)
# both indexes are included in a range and indexing starts from zero
print(get_range_sum(0,5))
update_segment_tree(3,10)
print(get_range_sum(0,5))

# # using segment_tree for min in range query
# def constuct_segment_tree():
#     segment_tree=[0]*(n<<1)
#     for i in range(n):
#         segment_tree[i+n]=array[i]
#     for i in range(n-1,0,-1):
#         segment_tree[i]=min(segment_tree[i<<1],segment_tree[i<<1 |1])
#     return segment_tree
# def update_segment_tree(index,new_value):
#     index += n
#     segment_tree[index]=new_value
#     while(index>0):
#         segment_tree[index>>1]=min(segment_tree[index],segment_tree[index^1])# xor left child with one = right child,xor right child with one = left child,
#         index>>=1
#     return
# def get_range_min(a,b):
#     # both indexes are included in a range and indexing starts from zero
#     a+=n
#     b+=n
#     ans=float("inf")
#     while(a<=b):
#         if(a & 1):#right child
#             ans=min(ans,segment_tree[a])
#             a+=1 # move right
#         if(not (b & 1)):#left child
#             ans=min(ans,segment_tree[b])
#             b-=1
#         a>>=1
#         b>>=1
#
#     return ans
#
#
# array =list(map(int,input().split()))
# n=len(array)
# array.extend([0]*(2**((n-1).bit_length())-n)) # nearest power of two#
# n=len(array)# new length(power of two)
# segment_tree=constuct_segment_tree()
# print(segment_tree)
# print(get_range_min(0,5))
# print(get_range_min(1,5))
# print(get_range_min(2,5))
# print(get_range_min(3,5))
# print(get_range_min(4,5))
# print(get_range_min(5,5))
