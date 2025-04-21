import pytest
from linked_list import LinkedList

@pytest.mark.skip()
def test_type_error():
	data = [1, 2, 3, 4, 5]
	instance = LinkedList(data)
	with pytest.raises(TypeError):
		instance['a'] = 1

@pytest.mark.skip()
@pytest.mark.parametrize("test_input", (5, -6))
def test_index_in_range_error(test_input):
	data = [1, 2, 3, 4, 5]
	instance = LinkedList(data)
	with pytest.raises(IndexError):
		instance[test_input] = 'T'

@pytest.mark.skip()
def test_slice_value_not_iterable():
	data = [1, 2, 3, 4, 5]
	instance = LinkedList(data)
	with pytest.raises(TypeError) as excinfo:
		instance[0:5] = 1
	print(str(excinfo))

if __name__ == "__main__":
	test_type_error()
	test_index_in_range_error()
	test_slice_value_not_iterable()