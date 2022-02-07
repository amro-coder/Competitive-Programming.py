# using segment tree for updating a range of values
# the idea is we build a difference array such that array[i]=sum(diff_array[0] to diff_array[i])
# then when we update a range all we have to do is increase (new_element - old_element) to the index of start of the range
# and decrease the element after the range by (new_element - old_element)
# explanation:
# changing a range of values will not change the diferences inside the range but will only change the differences in the first
# element and last element of the range
# so all we have to do is make a segment tree for the difference array
# and to get an element in index i all we have to do is get the sum from the beginning to i
# using the segment tree each operation will take O(log n)

def constuct_segment_tree(array):
    segment_tree=[0]*(n<<1)
    for i in range(n):
        segment_tree[i+n]=array[i]
    for i in range(n-1,0,-1):
        segment_tree[i]=segment_tree[i<<1]+segment_tree[i<<1 |1]
    return segment_tree
def update_segment_tree(a,b,value):
    a += n
    while(a>0):
        segment_tree[a]+=value
        a>>=1

    b += (n+1)
    while (b > 0):
        segment_tree[b] -= value
        b >>= 1

    return
def get_index_value(index):
    # both indexes are included in a range and indexing starts from zero
    a=0
    b=index
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


array =list(map(int,input().split()))+[0]#adding an element beacuse if we update a range ending in last element we should update the index+1
n=len(array)
array.extend([0]*(2**((n-1).bit_length())-n)) # nearest power of two#
n=len(array)
diff_array=[array[0]]
for i in range(1,n):
    diff_array.append(array[i]-array[i-1])
print(diff_array)
segment_tree=constuct_segment_tree(diff_array)
print(segment_tree)
print(get_index_value(0))
print(get_index_value(1))
print(get_index_value(2))
print(get_index_value(3))
update_segment_tree(0,3,10)
print(get_index_value(0))
print(get_index_value(1))
print(get_index_value(2))
print(get_index_value(3))





