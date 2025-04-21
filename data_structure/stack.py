from dataclasses import dataclass
from typing import Self

@dataclass(slots=True)
class Node:
	item: object
	_next: Self | None = None

"""
Stack flow is LIFO (Last in First out). LIFO - Take from the back, add to the back
Complexity: Push - O(1), Pop - O(1), Peek - O(1)
"""
class Stack:
	def __init__(self):
		self._head: Node | None = None
		self.length: int = 0

	def push(self, item:object) -> None:
		self.length += 1
		node = Node(item)

		if self.length == 1:
			self._head = node
			return

		node._next = self._head
		self._head = node

	def pop(self) -> object:
		if self.length == 0:
			return None

		item = self._head.item
		self._head = self._head._next
		self.length -= 1

		return item

	def peek(self) -> object:
		return self._head.item if self.length != 0 else None
