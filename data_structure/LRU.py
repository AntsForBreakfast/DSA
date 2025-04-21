from typing import Generic, TypeVar, Union
from dataclasses import dataclass

T = TypeVar('T')
K = TypeVar('K')
V = TypeVar('V')

@dataclass
class Node[T]:
	value: T
	next_: Union['Node[T]', None] = None
	prev: Union['Node[T]', None] = None

	def __hash__(self):
		return id(self)

	def __eq__(self, other):
		if not isinstance(other, Node):
			return NotImplemented

		return self.value == other.value

class LRU(Generic[K, V]):
	def __init__(self, capacity: int) -> None:
		self.capacity: int = capacity

		self._length: int = 0
		self._head: Node[V] | None = None
		self._tail: Node[V] | None = None
		self._lookup: Dict[K, Node[V]] = {}
		self._reverse_lookup: Dict[Node[V], K] = {}

	def update(self, key: K, value: V) -> None:
		node = self._lookup.get(key)

		if node is None:
			node = Node(value)
			self._length += 1
			self._prepend(node)
			self._trim_cache()

			self._lookup[key] = node
			self._reverse_lookup[node] = key

		else:
			self._detach(node)
			self._prepend(node)
			node.value = value

	def get(self, key: K) -> V | None:
		node = self._lookup.get(key)

		if node is None:
			return None

		self._detach(node)
		self._prepend(node)

		return node.value

	def _detach(self, node: Node[V]) -> None:
		if node.prev:
			node.prev.next_ = node.next_

		if node.next_:
			node.next_.prev = node.prev

		if self._head == node:
			self._head = self._head.next_

		if self._tail == node:
			self._tail = self._tail.prev

		node.next_ = None
		node.prev = None

	def _prepend(self, node: Node[V]) -> None:
		if self._head is None:
			self._head = self._tail = node
			return

		node.next_ = self._head
		self._head.prev = node

		self._head = node

	def _trim_cache(self) -> None: 
		if self._length <= self.capacity:
			return

		tail = self._tail
		self._detach(tail)

		key = self._reverse_lookup.pop(tail)
		self._lookup.pop(key)
		self._length -= 1
