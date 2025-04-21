from dataclasses import dataclass
from typing import Any

@dataclass
class Node:
	value: Any
	_next: 'Node | None' = None
	_prev: 'Node | None' = None

head = None

for letter in ('A', 'B', 'C', 'D'):
	node = Node(letter)

	if head is None:
		head = node
	else:
		temp = head
		prev = None
		while temp._next is not None:
			prev = temp
			temp = temp._next
		temp._next = node
		temp._prev = prev

print("Start |", head.value)
i = head._next
print('Next', i.value)
i = i._next
print("Next", i.value)
i = i._prev
print('Prev', i.value)