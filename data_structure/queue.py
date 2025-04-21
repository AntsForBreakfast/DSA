from dataclasses import dataclass
from typing import Self

@dataclass(slots=True)
class Node:
	item: object
	_next: Self | None = None

"""
Queue flow is FIFO (First in First out). FIFO - Take from the front, add at the back
Complexity: Push - O(1), Pop - O(1), Peek - O(1)
"""
class Queue:
	def __init__(self) -> None:
		self.length: int = 0
		self._head: Node | None = None
		self._tail: Node | None = None

	def enqueue(self, item: object) -> None:
		self.length += 1
		node = Node(item)

		if self.length == 1:
			self._tail = self._head = node
			return

		self._tail._next = node
		self._tail = node

	def deque(self) -> object:
		if self.length == 0:
			return None

		item = self._head.item
		self._head = self._head._next
		self.length -= 1

		return item

	def peek(self) -> object:
		return self.head.item if self.length != 0 else None
