import pytest

from linked_list import LinkedList


@pytest.mark.parametrize("test_input", 
	(
		("a",None, None),
		(None,3.5, None),
		(None,None,list())
	)
)
def test_index_type_error(test_input):
	data = [1, 2, 3, 4, 5]
	instance = LinkedList(data)
	start, stop, step = test_input
	with pytest.raises(TypeError):
		instance[start:stop:step]

if __name__ == '__main__':
	test_index_type_error()