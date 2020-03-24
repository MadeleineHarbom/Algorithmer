from Obligatorisk_Opgave_1.SplayTree import *

leTree = SplayTree()

node11 = Node(11)
leTree.insert(node11)
node8 = Node(8)
leTree.insert(node8)
node15 = Node(15)
leTree.insert(node15)
node3 = Node(3)
leTree.insert(node3)
node1 = Node(1)
leTree.insert(node1)
node12 = Node(12)
leTree.insert(node12)
node5 = Node(5)
leTree.insert(node5)

print(str(leTree.search(5).element))
print(str(leTree.access(node12).element))
print(leTree.root.element)
print(leTree.remove(node12).element)
print(leTree.remove(node3).element)



