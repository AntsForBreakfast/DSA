from dataclasses import dataclass
from typing import Self


# Compare 2 binary tress if they equal in shape and structure

@dataclass(slots=True)
class BinaryNode:
	value: object
	left: Self | None = None
	right: Self | None = None

def compare(a: BinaryNode, b: BinaryNode) -> bool:
	if a is None and b is None:
		return True

	if a is None or b is None:
		return False

	if a.value != b.value:
		return False

	return compare(a.left, b.left) and compare(a.right, b.right)

root_1: BinaryNode = BinaryNode(5)
root_1.left = BinaryNode(23)
root_1.left.left = BinaryNode(5)
root_1.left.right = BinaryNode(4)
root_1.right = BinaryNode(3)
root_1.right.left = BinaryNode(18)
root_1.right.right = BinaryNode(21)

root_2: BinaryNode = BinaryNode(5)
root_2.left = BinaryNode(23)
root_2.left.left = BinaryNode(5)
root_2.left.right = BinaryNode(4)
root_2.right = BinaryNode(3)
root_2.right.left = BinaryNode(18)
root_2.right.right = BinaryNode(21)


x = compare(root_1, root_2)
print(x)