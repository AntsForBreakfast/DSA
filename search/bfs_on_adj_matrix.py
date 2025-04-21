from dataclasses import dataclass
from typing import Self

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


type WeightedAdjacencyMatrix = list[list[int]]

def breadth_first_search(graph:WeightedAdjacencyMatrix, source:int, needle:int) -> list[int] | None:
	queue = Queue()

	# Used to keep the path to the needle
	prev = [-1]*len(graph)

	# Used to avoid duplicates in queue
	seen = [False]*len(graph)

	# Marking "source" as visited
	seen[source] = True

	# Pushing source to the queue
	queue.enqueue(source)

	while len(queue):
		# Pop from queue
		curr = queue.deque()

		# Needle was found
		if curr == needle:
			break

		# All neighbours of a node in a graph
		adjs = graph[curr]

		for i in range(len(adjs)):
			# 0 == not a neighbour
			if adjs[i] == 0 or seen[i]:
				continue

			# Neighbour found

			# Marking as seen
			seen[i] = True

			# Marking path
			prev[i] = curr

			# Add neigbour to the queue
			queue.enqueue(i)

	# Needle was not found
	if prev[needle] == -1:
		return None

	# Needle found, generate a path to the node
	curr = needle
	out: list[int] = []

	while prev[curr] != -1:
		out.append(curr)
		curr = prev[curr]

	return [[source] + out[::-1]]

matrix: WeightedAdjacencyMatrix = [
	[0, 1, 1, 1, 0, 0, 0, 0],
	[0, 0, 0, 0, 1, 0, 0, 0],
	[0, 1, 0, 1, 0, 0, 0, 0],
	[0, 1, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 1, 0, 0],
	[0, 0, 0, 0, 0, 0, 1, 0],
	[0, 0, 0, 0, 0, 0, 0, 1],
	[0, 0, 0, 0, 0, 0, 0, 0],
]


path = breadth_first_search(matrix, 0, 7)