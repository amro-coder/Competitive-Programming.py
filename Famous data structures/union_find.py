# Operation Running time
# Initialize O(n)
# Find O(log n)
# Union O(log n)

# the key opreation is unite we unite the set which contains the longest path as the parent with the other set so that we
# we only the longest find opreation remains as small as possiple.
# note that if we keep adding one element to a set we will always have the emelent attached to the parent of the set immediately
# the problem happens when we unite 2 sets with it's parents have at least one child, here we choose the set with the sohortet longest path
# to have it's parent point to the parent of the other set.
# turns out this whole complex idea can be implented with just comparing the size of the 2 sets and have the smaller size point to
# the bigger size and increase the size of the bigger size.
# notice this will not always be the best answer but it's gurenteed that it's O notation wil be O(log(size))
# example:
# parent=[0, 0, 0, 0, 0, 0, 8, 6, 8, 8]
# size=[6, 1, 1, 1, 1, 1, 2, 1, 4, 1]
# uniting 9 and 0 will produce:
# parent=[0, 0, 0, 0, 0, 0, 8, 6, 0, 8]
# size=[10, 1, 1, 1, 1, 1, 2, 1, 4, 1]
# longest path in this case is 3 , find_parent(7) 7->6->8->0
# but if we united 9 and 0 like this:
# parent=[8, 0, 0, 0, 0, 0, 8, 6, 6, 8]
# then the longest path will be 2 , find_parent(7) 7->6->8

def find_parent(x):
    while(x!=parent[x]):
        x=parent[x]
    return x

def unite(x,y):
    parent_x=find_parent(x)
    parent_y=find_parent(y)
    if parent_x!=parent_y:
        if size[parent_x]<size[parent_y]:
            parent_x,parent_y=parent_y,parent_x
#       parent_x has the bigger size
        size[parent_x]+=size[parent_y]
        parent[parent_y]=parent_x
        return True
    # returns false if x and y are in the same set
    return False



n=int(input())
parent=[i for i in range(n)]
size=[1]*n










