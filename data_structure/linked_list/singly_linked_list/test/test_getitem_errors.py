import pytest
from linked_list import LinkedList


@pytest.mark.parametrize("test_input", (5, -6))
def test_index_in_range_error(test_input):
	data = [1, 2, 3, 4, 5]
	instance = LinkedList(data)
	with pytest.raises(IndexError):
		instance[test_input]

def test_type_error():
	data = [1, 2, 3, 4, 5]
	instance = LinkedList(data)
	with pytest.raises(TypeError):
		instance['a']

def test_slice_step_zero_exception():
	data = [1, 2, 3, 4, 5]
	instance = LinkedList(data)
	with pytest.raises(ValueError):
		instance[::0]
		
if __name__ == "__main__":
	test_index_in_range_error()
	test_slice_step_zero_exception()
	test_type_error()