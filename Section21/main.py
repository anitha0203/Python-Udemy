from node import Node
from binary_tree import BinaryTree


left = Node(5)
head = Node(9)
right = Node(15)

head.left = left
head.right = right

print(head)
print(head.left)
print(head.right)

tree = BinaryTree(Node(9))
tree.add(Node(5))
tree.add(Node(11))

print(tree.head)
print(tree.head.left)
print(tree.head.right)

tree.inorder()
print(tree.find(11))
