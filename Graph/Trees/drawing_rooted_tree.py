# the idea is we give spaces to each node so that the left child and all it's children are on it's left,simiallry for right child
# that's why the root is always on a unique column
# notice that the only space that differ is the space right before the first child in each level
# because it only needs to ba padded so that its left child can have children
# but the genral case is that we need to put spaces before a node so that it can have a right child and the next node can have a left child
class Node:
    def __init__(self,value="",level=-1):
        self.level=level
        self.value=value
        self.left=None
        self.right=None
        self.parent=None
class binary_tree:
    def __init__(self):
        self.root=None
        self.nodes=0

    def bfs_levels(self):
        levels=[]
        levels.append([self.root])
        self.root.level=0
        self.nodes-=1
        while(self.nodes):
            levels.append([])
            for parent in levels[-2]:
                # left child
                if parent.left:
                    levels[-1].append(parent.left)
                    parent.left.level=parent.level+1
                    self.nodes-=1
                else:
                    levels[-1].append(Node(" ",parent.level+1))
                # right child
                if parent.right:
                    levels[-1].append(parent.right)
                    parent.right.level=parent.level+1
                    self.nodes-=1
                else:
                    levels[-1].append(Node(" ",parent.level+1))
        return levels

    def most_left(self):
        node=self.root
        while(node.left):
            node=node.left
        return node

    def print_tree(self):
        levels=self.bfs_levels()
        n=len(levels)
        spaces=[0]
        for i in range(n):
            spaces.append(2*spaces[-1]+1)
        spaces.reverse()

        most_left=self.most_left()
        spaces_to_removed=spaces[most_left.level+1]

        # printing the root
        print(" "*(spaces[1]-spaces_to_removed),self.root.value,sep='')
        last_padded=(spaces[1]-spaces_to_removed)-1
        for i in range(n-1):
            # we print the children of current level
            print(" "*(max(last_padded-spaces[i+2],0)),end='')
            last_padded=max(last_padded-spaces[i+2],0)-1
            if(levels[i+1][0].value!=" "):
                print(levels[i + 1][0].value, end=" " * spaces[i + 1])
            else:
                print(end=" "*spaces[i+1])
            for j in range(1,(1<<(i+1))):
                print(levels[i+1][j].value,end=" "*spaces[i+1])
            print()



tree=binary_tree()
tree.nodes=4
tree.root=Node(5)
tree.root.left=Node(6)
tree.root.right=Node(9)
tree.root.right.right=Node(1)
tree.print_tree()

