
class MinHeap:
	def __init__(self):
		self.heap: list[int] = []
		self._length: int = 0

	def insert(self, value:int) -> None:
		self._length += 1
		self.heap.append(value)

		child_idx = self._length-1
		parent_idx = (child_idx-1)//2

		while parent_idx >= 0 and self.heap[parent_idx] > value:
			self.heap[child_idx] = self.heap[parent_idx]
			self.heap[parent_idx] = value

			child_idx = parent_idx
			parent_idx = (child_idx-1)//2

	def delete(self) -> int|None:
		if not self.heap:
			return

		self._length -= 1
		value = self.heap[0]
		self.heap[0] = self.heap.pop()
		
		parent_idx = 0
		parent_value = self.heap[parent_idx]
		left_idx = 2*parent_idx + 1
		right_idx = 2*parent_idx + 2

		while left_idx < self._length or right_idx < self._length:
			if left_idx < self._length and right_idx < self._length:
				left_value = self.heap[left_idx]
				right_value = self.heap[right_idx]

				if left_value < right_value and left_value < parent_value:
					self.heap[parent_idx] = left_value
					self.heap[left_idx] = parent_value
					parent_idx = left_idx

				elif right_value < left_value and right_value < parent_value:
					self.heap[parent_idx] = right_value
					self.heap[right_idx] = parent_value
					parent_idx = right_idx

			elif left_idx < self._length:
				left_value = self.heap[left_idx]

				if left_value < parent_value:
					self.heap[parent_idx] = left_value
					self.heap[left_idx] = parent_value
					parent_idx = left_idx

			elif right_idx < self._length:
				right_value = self.heap[right_idx]
				
				if right_value < parent_value:
					self.heap[parent_idx] = right_value
					self.heap[right_idx] = parent_value
					parent_idx = right_idx
					
			else:
				break

			left_idx = 2*parent_idx + 1
			right_idx = 2*parent_idx + 2

		return value

heap = MinHeap()
heap.insert(3)
heap.insert(2)
heap.insert(1)
heap.insert(0)
heap.insert(69)
v = heap.delete()
print(v, heap.heap)
v = heap.delete()
print(v, heap.heap)
v = heap.delete()
print(v, heap.heap)
v = heap.delete()
print(v, heap.heap)