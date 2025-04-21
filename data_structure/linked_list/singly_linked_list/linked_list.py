from dataclasses import dataclass
from typing import Iterator, Iterable, Self, SupportsIndex, overload

@dataclass(slots=True)
class Node:
	value: object
	_next: Self | None = None

	def __eq__(self, other: object) -> bool:
		if not isinstance(other, Node):
			return NotImplemented

		node = self
		other_node = other
		while node is not None and other_node is not None:
			if node.value != other_node.value:
				return False

			node = node._next
			other_node = other_node._next

		return node is other_node

class LinkedList[T]:
	def __init__(self, value:Iterable|None = None):
		self._head: Node | None = None
		self._tail: Node | None = None
		self._length: int = 0

		if value is not None:
			self.extend(value)

	def __repr__(self) -> str:
		if self._head is not None:
			return f"LinkedList({self._head})"
		else:
			return "LinkedList()"

	def __len__(self) -> int:
		return self._length

	def __iter__(self) -> Iterator:
		if self._head is not None:
			node = self._head

			while node is not None:
				yield node.value
				node = node._next

	def __eq__(self, other) -> bool:
		if isinstance(other, LinkedList):
			return self._length == other._length and self._head == other._head
		else:
			return NotImplemented

	def _process_slice(self, index:slice) -> tuple[int,int,int]:
		"""Sets default values, converts to positive, clamps"""
		start, stop, step = index.start, index.stop, index.step

		if (
		    (not isinstance(start, int) and start is not None)
		    or (not isinstance(stop, int) and stop is not None)
		    or (not isinstance(step, int) and step is not None)
		):
		    raise TypeError(
		        "slice indices must be integers or None or have an __index__ method"
		    )

		length = self._length

		if step is None:
			step = 1
		elif step == 0:
			raise ValueError("slice step cannot be zero")

		if start is None:
			start = 0 if step > 0 else length-1
		elif start < 0:
			start = max(length + start, 0)
		elif start > length:
			start = length if step > 0 else length-1

		if stop is None:
			stop = length if step > 0 else -1
		elif stop < 0:
			stop = max(length + stop, -1)

		return start, stop, step

	@overload
	def __getitem__(self, index:SupportsIndex, /) -> T:
		...

	@overload
	def __getitem__(self, slice:'slice[SupportsIndex|None, SupportsIndex|None, SupportsIndex|None]', /) -> 'LinkedList[T]':
		...

	def __getitem__(self, index):
		if isinstance(index, SupportsIndex):
			# Clamping to data length
			if index >= self._length or index <= -self._length-1:
				raise IndexError("linked list index out of range")

			if index < 0:
				index = self._length+index

			for i, element in enumerate(self):
				if i != index:
					continue
				return element

		elif isinstance(index, slice):
			linked_list = LinkedList()

			# Return early if empty
			if self._head is None:
				return linked_list

			start, stop, step = self._process_slice(index)
			length = self._length
			
			if abs(step) >= length:
				linked_list.append(self[start])
				return linked_list

			node_indices = range(start, stop, step)

			# Not in range
			if not node_indices:
			    return linked_list

			last_index = node_indices[-1] if step > 0 else node_indices[0]
			for i, element in enumerate(self):
			    if i not in node_indices:
			        continue

			    linked_list.append(element)

			    if last_index == i:
			        break

			if step < 0:
				linked_list.reverse()

			return linked_list
		else:
			raise TypeError(f'list indices must be integers or slices, not {type(index).__name__}')

	@overload
	def __setitem__(self, index:SupportsIndex, value:object, /) -> None:
		...

	@overload
	def __setitem__(self, slice:'slice[SupportsIndex|None, SupportsIndex|None, SupportsIndex|None]', value:object, /) -> None:
		...
	# Partialy finished and tested
	def __setitem__(self, index, value) -> None:
		# Finished and tested
		if isinstance(index, SupportsIndex):
			# Clamping to data length
			if index >= self._length or index <= -self._length-1:
				raise IndexError("linked list index out of range")

			if index < 0:
				index = self._length+index

			node = self._head
			for _ in range(index):
				node = node._next

			node.value = value

		# Not finished and not tested
		elif isinstance(index, slice):
			prev_node = None
			current_node = self._head

			# If empty linked list
			if current_node is None:
				self.extend(value)
				return

			start, stop, step = self._process_slice(index)

			if step < 0:
				# Converting negative slice to postive
				negative_slice_range = range(start, stop, step)
				start = negative_slice_range[-1]
				stop = negative_slice_range[0]+1

				if hasattr(value, '__reversed__'):
					value = reversed(value)

			print(value)
			value = iter(value)

			for _ in range(start):
				prev_node = current_node
				current_node = current_node._next

			# Value needs better name since its iterable and have many values
			i = start

			for element in value:
				if current_node is None or i >= stop:
					node = Node(element)
					node._next = current_node
					prev_node._next = node
					prev_node = node

					self._length += 1
					continue
				
				current_node.value = element

				for _ in range(abs(step)):
					if current_node is None:
						break
					prev_node = current_node
					current_node = current_node._next
					i += 1

			if i < stop:
				while i!= stop:
					if current_node is None:
						break
					current_node = current_node._next
					self._length -= 1
					i += 1

				prev_node._next = current_node

			print('\nI:', i)
			print('Head:', self._head)
			print('prev_node:', prev_node)
			print('current node:', current_node)
			print(start, stop, step)
			print('value:', value)

		else:
			raise TypeError(f'linked list indices must be integers or slices, not {type(index).__name__}')

	# Not finished and not tested
	def __delitem__(self, index: int) -> None:
		if not isinstance(index, int):
			raise TypeError("slice indices must be integers")

		elif index > self._length-1 or self._head is None:
			raise IndexError("linked list index out of range")

		node = self._head
		prev_node = None
		count = 0
		while count != index:
			prev_node = node
			node = node._next
			count += 1

		if index == 0:
			self._head = None if self._length == 1 else node._next

		elif index == self._length-1:
			prev_node._next = None
		else:
			prev_node._next = node._next

		self._length -= 1

	# Not finished and not tested
	def append(self, value: object) -> None:
		node = Node(value)

		if self._head is None:
			self._head = node
			self._tail = node
			self._length = 1
			return

		self._tail._next = node
		self._tail = self._tail._next
		self._length += 1

	# Not finished and not tested
	def extend(self, value: Iterable) -> None:
		for i in value:
			self.append(i)

	# Not finished and not tested
	def insert(self, index:int, value:object) -> None:
		if index == 0:
			self.prepend(value)
			return

		if index > len(self):
			self.append(value)
			return
			
		node = Node(value)

		if 0 < index <= len(self):
			n = None
			for i in range(index):
				if n is None:
					n = self._head
					continue
				n = n._next

			node._next = n._next
			n._next = node

	# Not finished and not tested
	def remove(self, value: object) -> None:
		node = self._head
		prev_node = node
		found = False

		while node._next is not None:
			if value == node.value:
				found = True
				break

			prev_node = node
			node = node._next

		if found:
			prev_node._next = node._next
		else:
			raise ValueError('remove(x): x not in linked list')

	# Not finished and not tested
	def pop(self, index=None) -> object:
		if self._length < 1:
			raise IndexError("pop from empty linked list")
		if self._length - 1 < index:
			raise IndexError("pop index out of linked list range")

		value = None

		if index is None:
			value = self[self._length-1]
			del self[self._length-1]
		else:
			value = self[index]
			del self[index]

		return value

	# Not finished and not tested
	def clear(self) -> None:
		self._head = None
		self._tail = None

	# Not finished and not tested
	def index(self, value:object, start:int = 0, stop:int = -1) -> int:
		values = list(self)

		if stop == -1:
			stop = self._length

		index_counter = start
		while index_counter != stop:
			if values[index_counter] == value:
				return index_counter
			index_counter+=1
		else:
			raise ValueError(f"{value} is not in linked list")

	# Not finished and not tested
	def count(self, value:object) -> int:
		count = 0

		for item in self:
			if item==value:
				count+=1
		return count

	# Not finished and not tested
	def prepend(self, value: object) -> None:
		node = Node(value)

		if self._head is None:
			self._head = node
			self._tail = node
		else:
			node._next = self._head
			self._head = node

		self._length += 1

	# Not finished and not tested
	def reverse(self) -> None:
		values = list(self)
		length = round(self._length/2)

		for n in range(length):
			left = values[n]
			values[n] = values[self._length-n-1]
			values[self._length-n-1] = left

		node = self._head
		for v in values:
			node.value = v
			node = node._next

	# Not finished and not tested
	def copy(self) -> Self:
		instance = LinkedList()
		instance.extend(self)
		return instance
