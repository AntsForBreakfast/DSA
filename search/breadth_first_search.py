from dataclasses import dataclass
from typing import Self

@dataclass(slots=True)
class BinaryNode:
	value: object
	left: Self | None = None
	right: Self | None = None

@dataclass(slots=True)
class Node:
	item: object
	_next: Self | None = None

class Queue:
	def __init__(self) -> None:
		self._length: int = 0
		self._head: Node | None = None
		self._tail: Node | None = None

	def __len__(self) -> int:
		return self._length

	def enqueue(self, item: object) -> None:
		self._length += 1
		node = Node(item)

		if len(self) == 1:
			self._tail = self._head = node
			return

		self._tail._next = node
		self._tail = node

	def deque(self) -> object:
		if len(self) == 0:
			return None

		item = self._head.item
		self._head = self._head._next
		self._length -= 1

		return item

	def peek(self) -> object:
		return self.head.item if self.length != 0 else None


"""
	Breadth-first-search on binary tree
	For breath-first-search is used a queue data structure
"""

def breadth_search(bn: BinaryNode, value:int) -> int:
	queue = Queue()
	queue.enqueue(bn)

	while queue:
		bnode = queue.deque()

		if bnode.value == value:
			return True

		if bnode.left:
			queue.enqueue(bnode.left)
		if bnode.right:
			queue.enqueue(bnode.right)

	return False


root: BinaryNode = BinaryNode(7)
root.left = BinaryNode(23)
root.left.left = BinaryNode(5)
root.left.right = BinaryNode(4)
root.right = BinaryNode(3)
root.right.left = BinaryNode(18)
root.right.right = BinaryNode(21)


x = breadth_search(root, 23)
print(x)