import pytest
from linked_list import LinkedList

@pytest.mark.parametrize("test_input, expected", 
	(
		(["Hello World!"], ["Hello World!"]),
		([12345], [12345]),
		([3.145], [3.145]),
		([3j], [3j]),
		([True], [True]),
		(["Hello World!", 12345, 3.145, 3j], ["Hello World!", 12345, 3.145, 3j]),
		(("Hello World!", 12345, 3.145, 3j), ["Hello World!", 12345, 3.145, 3j]),
		({1:10, 2:20, 3:30}, [1,2,3]),
		({1,3,5,5}, [1,3,5])
	)
)
def test_constructor_makes_equal_sequence(test_input, expected):
	instance = LinkedList(test_input)
	assert list(instance) == expected

if __name__ == "__main__":
	test_constructor_makes_equal_sequence()