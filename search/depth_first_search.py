from dataclasses import dataclass
from typing import Self

@dataclass(slots=True)
class BinaryNode:
	value: object
	left: Self | None = None
	right: Self | None = None



def search(node: BinaryNode|None, item:int) -> bool:
	if node is None:
		return False

	if node.value == item:
		return True

	if node.value >= item:
		return search(node.left, item)

	return search(node.right, item)

	return False

def dfs(node:BinaryNode, item:int) -> bool:
	return search(node, item)


root: BinaryNode = BinaryNode(25)
root.left = BinaryNode(20)
root.left.right = BinaryNode(22)
root.left.left = BinaryNode(10)
root.left.left.right = BinaryNode(12)
root.left.left.right.right = BinaryNode(15)
root.left.left.left = BinaryNode(5)
root.left.left.left.left = BinaryNode(1)
root.left.left.left.right = BinaryNode(8)

root.right = BinaryNode(36)
root.right.left = BinaryNode(30)
root.right.left.left = BinaryNode(28)
root.right.right = BinaryNode(40)
root.right.right.left = BinaryNode(38)
root.right.right.right = BinaryNode(48)
root.right.right.right.left = BinaryNode(45)
root.right.right.right.right = BinaryNode(50)

x = dfs(root, 28)
print(x)