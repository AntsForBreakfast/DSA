from typing import Iterable

def linear_search(iterable: Iterable[int], search: int) -> bool:
	for element in iterable:
		if element == search:
			return True
	return False


def recursive_linear_search(iterable:Iterable[int], search:int, start_index: int = 0) -> bool:
	# checking if index in bounds
	if start_index >= len(iterable):
		return False

	element = iterable[start_index]
	if element == search:
		return True

	start_index += 1
	return recursive_linear_search(iterable, search, start_index)
