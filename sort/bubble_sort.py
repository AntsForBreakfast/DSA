"""Bubble sort is sort in place algorithm, 
it works by checking if next value is greater than current one if it is swamp em else move to the next value and repeat that.
It always move greater value to the end of container"""
def bubble_sort(data:list[str]) -> list[str]:
	length = len(data)

	while length > 1:
		for n in range(length-1):
			if data[n] > data[n+1]:
				element_a = data[n+1]
				element_b = data[n]

				data[n] = element_a
				data[n+1] = element_b
		length -= 1

	return data

def recursive_bubble_sort(data:list[str], data_length:int) -> list[str]:
	for n in range(data_length-1):
		if data[n] > data[n+1]:
			element = data.pop(n+1)
			data.insert(n, element)

	data_length -=1

	if data_length > 1:
		return recursive_bubble_sort(data, data_length)
	return data



x = [1,3,2,4,6,5,9,8,7]
print(x)
a = bubble_sort(x)
print(a)