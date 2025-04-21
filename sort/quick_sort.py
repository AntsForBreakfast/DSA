'''Quick sort - divide and conquer strategy'''

def sort(data: list[int], lo: int, hi: int) -> None:
	if lo >= hi:
		return

	pivot_idx = partition(data, lo, hi)

	sort(data, lo, pivot_idx - 1)
	sort(data, pivot_idx + 1, hi)

def partition(data: list[int], lo: int, hi: int) -> int:
	pivot = data[hi]
	idx = lo - 1

	for i in range(lo, hi):
		if data[i] <= pivot:
			idx += 1
			tmp = data[i]
			data[i] = data[idx]
			data[idx] = tmp

	idx += 1
	data[hi] = data[idx]
	data[idx] = pivot

	return idx

def quick_sort(data: list[int]) -> None:
	sort(data, 0, len(data)-1)
