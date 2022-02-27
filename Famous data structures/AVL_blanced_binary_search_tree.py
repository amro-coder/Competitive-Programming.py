class Node:
    def __init__(self, value=None, parent=None):
        self.contained_nodes = 1
        self.value = value
        self.parent = parent
        self.height = 1 if value != None else 0
        self.left = None
        self.right = None


class AVL():
    def __init__(self):
        self.__root = None
        return

    def __get_hight(self, node):
        return node.height if node else 0

    def __update_height(self, node):
        if (node):
            node.height = 1 + max(self.__get_hight(node.left), self.__get_hight(node.right))

    def __update_parents_height(self, node):
        # start updating from parent
        while (node != None):
            self.__update_height(node)
            node = node.parent
        return

    def __get_contained_nodes(self, node):
        return node.contained_nodes if node else 0

    def __update_contained_nodes(self, node):
        node.contained_nodes = 1 + self.__get_contained_nodes(node.left) + self.__get_contained_nodes(node.right)

    def __update_parents_contained_nodes(self, node):
        # start updating from node
        while (node != None):
            self.__update_contained_nodes(node)
            node = node.parent
        return

    def __rebalnce_AVL(self, node):
        while (node):
            diff = self.__get_hight(node.left) - self.__get_hight(node.right)
            new_root = node
            ancestor_node = node.parent
            #  case left left
            if (diff > 1 and self.__get_hight(node.left.left) >= self.__get_hight(node.left.right)):
                new_root = self.__right_rotate(node)
            #  case left right
            elif (diff > 1 and self.__get_hight(node.left.left) <= self.__get_hight(node.left.right)):
                node.left = self.__left_rotate(node.left)
                new_root = self.__right_rotate(node)
            # case right right
            elif (diff < -1 and self.__get_hight(node.right.right) >= self.__get_hight(node.right.left)):
                new_root = self.__left_rotate(node)
            # case right left
            elif (diff < -1 and self.__get_hight(node.right.right) <= self.__get_hight(node.right.left)):
                node.right = self.__right_rotate(node.right)
                new_root = self.__left_rotate(node)

            # update root if needed
            if (node == self.__root):
                self.__root = new_root
            # update ancestor node
            if (ancestor_node and node == ancestor_node.right):
                ancestor_node.right = new_root
                self.__update_height(ancestor_node)
            # parent node is a left child
            elif (ancestor_node and node == ancestor_node.left):
                ancestor_node.left = new_root
                self.__update_height(ancestor_node)
            # update next parent node
            node = node.parent

    def __left_rotate(self, node):
        # saving values in variables
        parent_node = node.parent
        x = node.right
        y = x.left
        # preforming the rotation
        node.right = y
        x.left = node

        node.parent = x
        x.parent = parent_node
        if (y):
            y.parent = node
        # updating heights and contained nodes
        self.__update_height(node)
        self.__update_height(x)
        self.__update_contained_nodes(node)
        self.__update_contained_nodes(x)
        # return the new root
        return x

    def __right_rotate(self, node):
        parent_node = node.parent
        # saving values in variables
        x = node.left
        y = x.right
        # preforming the rotation
        node.left = y
        x.right = node

        node.parent = x
        x.parent = parent_node
        if (y):
            y.parent = node
        # updating heights
        self.__update_height(node)
        self.__update_height(x)
        self.__update_contained_nodes(node)
        self.__update_contained_nodes(x)
        # return the new root
        return x

    def __get_min(self, node):
        min = None
        while (node):
            min = node
            node = node.left
        return min

    def __get_max(self, node):
        max = None
        while (node):
            max = node
            node = node.right
        return max

    def __delete(self, value):
        location = self.__contains__(value)
        if (not location):
            # value dosent exist
            return None

        # if node has no child (leaf node)
        if not location.right and not location.left:
            # node is the root
            if location == self.__root:
                self.__root = None
                return None
            # node is the left child of parent
            if location.parent.left == location:
                location.parent.left = None
                self.__update_parents_height(location.parent)
                self.__update_parents_contained_nodes(location.parent)
            else:
                # node is a right child to parent
                location.parent.right = None
                self.__update_parents_height(location.parent)
                self.__update_parents_contained_nodes(location.parent)
            return location.parent

        # node has only one child and it's right
        if location.right and not location.left:
            # node is the root
            if location == self.__root:
                self.__root = location.right
                location.right.parent = None
                return None
            # node is the left child of parent
            if location.parent.left == location:
                location.parent.left = location.right
                location.right.parent = location.parent
                self.__update_parents_height(location.parent)
                self.__update_parents_contained_nodes(location.parent)
            else:
                # node is a right child to parent
                location.parent.right = location.right
                location.right.parent = location.parent
                self.__update_parents_height(location.parent)
                self.__update_parents_contained_nodes(location.parent)
            return location.parent

        # node has only one child and it's left
        if location.left and not location.right:
            # node is the root
            if location == self.__root:
                self.__root = location.left
                location.left.parent = None
                return None
            # node is the left child of parent
            if location.parent.left == location:
                location.parent.left = location.left
                location.left.parent = location.parent
                self.__update_parents_height(location.parent)
                self.__update_parents_contained_nodes(location.parent)
            else:
                # node is a right child to parent
                location.parent.right = location.left
                location.left.parent = location.parent
                self.__update_parents_height(location.parent)
                self.__update_parents_contained_nodes(location.parent)
            return location.parent

        # node has two children
        min_node = self.__get_min(location.right)
        start_node_to_be_changed = min_node.parent if min_node.parent != location else min_node
        # updating the parent of the min node to swap with location
        # min_node is a right child
        if min_node.parent.right == min_node:
            # min node has a right child
            if (min_node.right):
                min_node.parent.right = min_node.right
                min_node.right.parent = min_node.parent
            else:
                min_node.parent.right = None
        # min node is a left child
        else:
            if (min_node.right):
                min_node.parent.left = min_node.right
                min_node.right.parent = min_node.parent
            else:
                min_node.parent.left = None

        # updating min_node as the new location
        min_node.right = location.right
        min_node.left = location.left
        if (location.right):
            location.right.parent = min_node
        if location.left:
            location.left.parent = min_node
        min_node.parent = location.parent

        if self.__root == location:
            self.__root = min_node
        else:
            if location.parent.right == location:
                location.parent.right = min_node
            else:
                location.parent.left = min_node

        # updating all parents
        self.__update_parents_height(start_node_to_be_changed)
        self.__update_parents_contained_nodes(start_node_to_be_changed)
        return start_node_to_be_changed

    def __contains__(self, value):
        node = self.__root
        while (node):
            if (value == node.value):
                return node
            elif (value > node.value):
                node = node.right
            else:
                node = node.left
        return None

    def __len__(self) -> int:
        return self.__root.contained_nodes if self.__root else 0

    def __str__(self):
        return str(self.get_ordered_values())

    def __iter__(self):
        return iter(self.get_ordered_values())

    def __delitem__(self, key):
        self.delete_by_value(self[key])
        return

    def __getitem__(self, index):
        if (index < 0):
            index = len(self) + index

        if (index >= len(self)):
            raise IndexError("index out of range")

        node = self.__root
        while (index != self.__get_contained_nodes(node.left)):
            if (index > self.__get_contained_nodes(node.left)):
                index -= (self.__get_contained_nodes(node.left) + 1)
                node = node.right
            else:
                node = node.left
        return node.value

    def delete_by_value(self, value):
        start_node_to_be_rebalanced = self.__delete(value)
        if (start_node_to_be_rebalanced):
            self.__rebalnce_AVL(start_node_to_be_rebalanced)

    def insert(self, value):
        if (self.__root == None):
            self.__root = Node(value)
            return
        proper_place = self.__root
        while (True):
            if (value <= proper_place.value):
                if (proper_place.left):
                    proper_place = proper_place.left
                else:
                    proper_place.left = Node(value, proper_place)
                    self.__update_parents_contained_nodes(proper_place)
                    if (proper_place.right == None):
                        self.__update_parents_height(proper_place)
                        self.__rebalnce_AVL(proper_place)
                    return
            else:
                if (proper_place.right):
                    proper_place = proper_place.right
                else:
                    proper_place.right = Node(value, proper_place)
                    self.__update_parents_contained_nodes(proper_place)
                    if (proper_place.left == None):
                        self.__update_parents_height(proper_place)
                        self.__rebalnce_AVL(proper_place)
                    return

    def get_ordered_values(self):
        x = []
        queue = [self.__root]
        while (queue):
            # since we pop from last element then we can insert elements in reversed order so that we always pop in right order
            node = queue.pop()
            if (type(node) != Node):
                x.append(node)
            else:
                if (node.right):
                    queue.append(node.right)
                queue.append(node.value)
                if (node.left):
                    queue.append(node.left)

        return x

    def find_bigger(self, value):
        # returns the index of the first value bigger than the given value, if it dosent exisit then the lenght is returned
        node = self.__root
        index = 0
        while (node):
            if (value >= node.value):
                index += self.__get_contained_nodes(node.left) + 1
                node = node.right
            else:
                node = node.left
        return index

    def find_equal_or_bigger(self, value):
        # returns the index of the first value equal or bigger than the given value, if it dosent exisit then the lenght is returned.
        # if multiple ocurencess of the wanted value exisit then a random index is given
        node = self.__root
        index = 0
        while (node):
            if (value == node.value):
                return index + self.__get_contained_nodes(node.left)
            elif (value > node.value):
                index += self.__get_contained_nodes(node.left) + 1
                node = node.right
            else:
                node = node.left
        return index

    def min_n_elements(self, num):
        if (num > len(self)):
            raise IndexError("number of elements wanted is bigger than the length")
        x = []
        queue = [self.__root]
        while (num):
            # since we pop from last element then we can insert elements in reversed order so that we always pop in right order
            node = queue.pop()
            if (type(node) != Node):
                num -= 1
                x.append(node)
            else:
                if (node.right):
                    queue.append(node.right)
                queue.append(node.value)
                if (node.left):
                    queue.append(node.left)

        return x

    def max_n_elements(self, num):  # fix this man
        if (num > len(self)):
            raise IndexError("number of elements wanted is bigger than the length")
        x = []
        queue = [self.__root]
        while (num):
            # since we pop from last element then we can insert elements in reversed order so that we always pop in right order
            node = queue.pop()
            if (type(node) != Node):
                num -= 1
                x.append(node)
            else:
                if (node.left):
                    queue.append(node.left)
                queue.append(node.value)
                if (node.right):
                    queue.append(node.right)
        x.reverse()
        return x