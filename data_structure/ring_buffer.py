"""
Ring buffer
"""
class RingBuffer:
	def __init__(self, capacity:int) -> None:
		self._capacity: int = capacity

		self.write_idx:int = 0
		self.read_idx:int = 0
		self.data: list[object] = [None]*self._capacity

	def enqueue(self, item: object) -> None:
		idx = self.write_idx%self._capacity
		self.data[idx] = item
		self.write_idx += 1

	def dequeue(self) -> object:
		print(self.read_idx, self.write_idx)
		if self.read_idx == self.write_idx:
			raise IndexError('Ring buffer out of elements')

		value = self.data[self.read_idx]
		self.read_idx += 1
		return value

buffer = RingBuffer(3)
buffer.enqueue('A')
buffer.enqueue('B')
buffer.enqueue('C')
print(buffer.data)
print(buffer.dequeue())
print(buffer.dequeue())
print(buffer.dequeue())
print(buffer.dequeue())
print(buffer.data)