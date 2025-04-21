import pytest
from linked_list import LinkedList

def test_all_none():
	data = [1,2,3,4,5]
	instance = LinkedList(data)
	assert instance._process_slice(slice(None,None,None)) == (0, 5, 1)

def test_step_is_none():
	data = [1,2,3,4,5]
	instance = LinkedList(data)
	assert instance._process_slice(slice(0, 5, None)) == (0, 5, 1)

def test_start_is_none_and_step_greater_than_zero():
	data = [1,2,3,4,5]
	instance = LinkedList(data)
	assert instance._process_slice(slice(None, 5, 1)) == (0, 5, 1)

def test_start_is_none_and_step_less_than_zero():
	data = [1,2,3,4,5]
	instance = LinkedList(data)
	assert instance._process_slice(slice(None, 5, -1)) == (4, 5, -1)

@pytest.mark.parametrize('test_input, expected',
	(
		((-1, 1, 1), (4, 1, 1)),
		((-60, 1, 1), (0, 1, 1))
	)
)
def test_start_is_negative(test_input, expected):
	'''converting negative start to postive start and clamping'''
	data = [1,2,3,4,5]
	instance = LinkedList(data)
	assert instance._process_slice(slice(*test_input)) == expected

def test_start_greater_than_length_and_step_greater_than_zero():
	data = [1,2,3,4,5]
	instance = LinkedList(data)
	assert instance._process_slice(slice(50, 1, 1)) == (5, 1, 1)

def test_start_greater_than_length_and_step_less_than_zero():
	data = [1,2,3,4,5]
	instance = LinkedList(data)
	assert instance._process_slice(slice(50, 1, -1)) == (4, 1, -1)

def test_stop_is_none_and_step_greater_than_zero():
	data = [1,2,3,4,5]
	instance = LinkedList(data)
	assert instance._process_slice(slice(0, None, 1)) == (0, 5, 1)

def test_stop_is_none_and_step_less_than_zero():
	data = [1,2,3,4,5]
	instance = LinkedList(data)
	assert instance._process_slice(slice(0, None, -1)) == (0, -1, -1)

@pytest.mark.parametrize('test_input, expected',
	(
		((1, -3, 1), (1, 2, 1)),
		((1, -90, 1), (1, -1, 1)),
	)
)
def test_stop_is_negative(test_input, expected):
	'''converting negative stop to positive stop and clamping'''
	data = [1,2,3,4,5]
	instance = LinkedList(data)
	assert instance._process_slice(slice(*test_input)) == expected

if __name__ == "__main__":
	test_all_none()
	test_step_is_none()
	test_start_is_none_and_step_greater_than_zero()
	test_start_is_none_and_step_less_than_zero()
	test_start_is_negative()
	test_start_greater_than_length_and_step_greater_than_zero()
	test_start_greater_than_length_and_step_less_than_zero()
	test_stop_is_none_and_step_greater_than_zero()
	test_stop_is_negative()