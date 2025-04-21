import pytest
from linked_list import LinkedList


@pytest.mark.parametrize("test_input",(0,2,-1,-3))
def test_index(test_input):
	data = [1, 2, 3, 4, 5]
	instance = LinkedList(data)
	assert instance[test_input] == data[test_input]

def test_slice_makes_copy():
	data = [1, 2, 3, 4, 5]
	instance = LinkedList(data)
	copy = instance[:]
	assert not (instance is copy)

def test_slice_empty_makes_equal_copy():
	data = [1, 2, 3, 4, 5]
	instance = LinkedList(data)
	copy = instance[:]
	assert instance == copy

@pytest.mark.parametrize('test_input', (6, -6))
def test_slice_step_greater_than_length(test_input):
	data = [1, 2, 3, 4, 5]
	instance = LinkedList(data)
	assert instance[::test_input] == LinkedList(data[::test_input])

@pytest.mark.parametrize('test_input', (5, -5))
def test_slice_step_equal_to_length(test_input):
	data = [1, 2, 3, 4, 5]
	instance = LinkedList(data)
	assert instance[::test_input] == LinkedList(data[::test_input])

def test_slice_over_empty():
	instance = LinkedList()
	assert instance._head is None and instance[::1] == LinkedList([][::1])

@pytest.mark.parametrize("test_input", 
	(
		(3,2,None),
		(3,2,1),
		(3,2,2),
		(2,2,None),
		(2,2,1),
		(2,2,2),
		(2,2,-1),
		(2,2,-2),
		(2,4,-1),
		(2,4,-2),
		(-2,-2,None),
		(-2,-2,1),
		(-2,-2,2),
		(-2,-2,-1),
		(-2,-2,-2),
		(-2,-3,None),
		(-2,-3,-1),
		(-2,-3,-2),
		(-2,-3,1),
		(-2,-3,2),
	)
)
def test_slice_not_in_range(test_input):
	data = [1, 2, 3, 4, 5]
	instance = LinkedList(data)
	start, stop, step = test_input
	assert instance[start:stop:step] == LinkedList(data[start:stop:step])

@pytest.mark.parametrize("test_input", 
	(
		(None,None,-1),
		(None,None,-2),
		(2, None, -1),
		(2, None, -2),
		(4, 1, -1),
		(4, 1, -2),
		(-1, None, -1),
		(-1, None, -2),
		(None, -4, -1),
		(None, -4, -2),
		(-1, -4, -1),
		(-1, -4, -2),
		(None, None, -20)
	)
)
def test_slice_negative_step_reverse_sequence(test_input):
	data = [1, 2, 3, 4, 5]
	instance = LinkedList(data)
	start, stop, step = test_input
	assert instance[start:stop:step] == LinkedList(data[start:stop:step])

@pytest.mark.parametrize("test_input",
	(
		(0, None, None),
		(-5, None, None),
		(None, 3, None),
		(None,-1, None),
		(None, None, 1),
		(None, None, 2),
		(-5, -1, None),
		(0, 5, None),
		(-1, None, None),
		(0, 1, 1),
		(2, None, 9),
		(-20, None, None),
		(20, None, None),
		(None, 20, None),
		(None, -20, None),
		(None, None, 20),
	)
)
def test_slice(test_input):
	data = [1, 2, 3, 4, 5]
	instance = LinkedList(data)
	start, stop, step = test_input
	assert instance[start:stop:step] == LinkedList(data[start:stop:step])


if __name__ == "__main__":
	test_index()
	test_slice_makes_copy()
	test_slice_empty_makes_equal_copy()
	test_slice_step_greater_than_length()
	test_slice_step_equal_to_length()
	test_slice_not_in_range()
	test_slice_negative_step_reverse_sequence()
	test_slice_over_empty()
	test_slice()