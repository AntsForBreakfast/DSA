from dataclasses import dataclass
from typing import Self

@dataclass(slots=True)
class BinaryNode:
	value: object
	left: Self | None = None
	right: Self | None = None

def walk(node: BinaryNode, path: list[int]) -> None:
	if node is None:
		return path

	# pre
	
	# recurse
	walk(node.left, path)
	path.append(node.value)
	walk(node.right, path)

	# post
	return path

def in_order_search(root) -> None:
	return walk(root, [])

root: BinaryNode = BinaryNode(7)
root.left = BinaryNode(23)
root.left.left = BinaryNode(5)
root.left.right = BinaryNode(4)
root.right = BinaryNode(3)
root.right.left = BinaryNode(18)
root.right.right = BinaryNode(21)

_in = in_order_search(root)
print(_in)