
class Node:

    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None
        self.parent = None


class SplayTree:

    def __init__(self):
        self.root = None


    def insert(self, node):
        if self.root is None:
            self.root = node
        else:
            done = False
            current = self.root
            while not done:
                if node.element < current.element:
                    if current.left is None:
                        current.left = node
                        node.parent = current
                        self.splay(node)
                        done = True
                    else:
                        current = current.left
                elif node.element > current.element:
                    if current.right is None:
                        current.right = node
                        node.parent = current
                        self.splay(node)
                        done = True
                    else:
                        current = current.right
                else:
                    print('Skal de komme være ens?')
                    done = True
        return node

    def remove(self, node):
        if self.root is None:
            return self.root
        self.splay(node)
        root1 = self.root.left
        root2 = self.root.right
        if root1 is None:
            self.root = root2
            return self.root
        else:
            maxxx = self.root
            while maxxx.right is not None:
                maxxx = maxxx.right
            self.splay(maxxx)
            root1.right = root2
            self.root = root1
        return self.root



    def splay(self, node):
        while node != self.root:
            parent = node.parent
            grandparent = node.parent.parent
            if grandparent is None:
                self.rotate(node)
            elif (parent == grandparent.left) == (node == parent.left):
                self.rotate(parent)
                self.rotate(node)
            else:
                self.rotate(node)
                self.rotate(node)
        return None


    def rotate(self, node: Node):
        parent = node.parent
        grand_parent = node.parent.parent


        if parent.right == node:
            left = node.left
            node.left = parent
            parent.right = left
        elif parent.left == node:
            right = node.right
            node.right = parent
            parent.left = right
        node.parent = grand_parent
        parent.parent = node
        if node.parent is None:
            self.root = node


    def search(self, element):
        current = self.root
        while True:
            if current.element == element:
                return current
            elif current.element > element:
                if current.right is None:
                    return None
                else:
                    current = current.right
            elif current.element < element:
                if current.left is None:
                    return None
                else:
                    current = current.left


    def access(self, node):
        self.splay(node)
        return self.root
