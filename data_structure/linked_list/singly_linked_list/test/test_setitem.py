import pytest
from linked_list import LinkedList


@pytest.mark.parametrize("test_input, expected",
	(
		(0, ('T', 2, 3, 4, 5)),
		(2, (1, 2, 'T', 4, 5)),
		(4, (1, 2, 3, 4, 'T')),
		(-5, ('T', 2, 3, 4, 5)),
		(-3, (1, 2, 'T', 4, 5)),
		(-1, (1, 2, 3, 4, 'T')),
	)
)

def test_index_assigment(test_input, expected):
	data = (1, 2, 3, 4, 5)
	instance = LinkedList(data)
	instance[test_input] = 'T'
	assert instance == LinkedList(expected)

@pytest.mark.parametrize("test_input, expected",
	(
		(((None, 3, 1), 'AB'), ('A', 'B', 4, 5)),
		(((3, None, 1), 'AB'), (1, 2, 3, 'A', 'B')),
		(((1, 3, 1), 'AB'), (1, 'A', 'B', 4, 5)),
	)
)
def test_slice_assigment_with_bigger_slice_than_iter(test_input, expected):
	data = (1,2,3,4,5)
	instance = LinkedList(data)

	(start, stop, step), iterable = test_input
	instance[start:stop:step] = iterable

	assert instance == LinkedList(expected)

@pytest.mark.parametrize(
    "test_input, expected",
    (
        (
            ((None, 3, 1), "ABCDEFGH"),
            ("A", "B", "C", "D", "E", "F", "G", "H", 4, 5),
        ),
        (
            ((3, None, 1), "ABCDEFGH"),
            (1, 2, 3, "A", "B", "C", "D", "E", "F", "G", "H"),
        ),
        (
            ((1, 3, 1), "ABCDEFGH"),
            (1, "A", "B", "C", "D", "E", "F", "G", "H", 4, 5),
        ),
    ),
)
def test_slice_assigment_with_smaller_slice_than_iter(test_input, expected):
	data = (1,2,3,4,5)
	instance = LinkedList(data)

	(start, stop, step), iterable = test_input
	instance[start:stop:step] = iterable

	assert instance == LinkedList(expected)


def test_slice_assigment_positive_step():
	data = (1,2,3,4,5)
	instance = LinkedList(data)

	instance[::2] = 'ABC'

	assert instance == LinkedList(('A', 2, 'B', 4, 'C'))

@pytest.mark.parametrize('test_input, expected',
	(
		(
			((None, None, -2), 'ABC'),
			('C', 2, 'B', 4, 'A'),
		),
		(
			((0, None, -2), 'A'),
			('A', 2, 3, 4, 5),
		),
		(
			((None, 3, -2), 'A'),
			(1, 2, 3, 4, 'A'),
		),
		(
			((1, 3, -2), ''),
			(1, 2, 3, 4, 5),
		),
		(
			((3, 1, -2), 'A'),
			(1, 2, 3, 'A', 5),
		),
	)
)
def test_slice_assigment_negative_step(test_input, expected):
	data = (1,2,3,4,5)
	instance = LinkedList(data)

	(start, stop, step), iterable = test_input
	instance[start:stop:step] = iterable
	
	assert instance == LinkedList(expected)

if __name__ == "__main__":
	test_index_assigment()
	test_slice_assigment_with_bigger_slice_than_iter()
	test_slice_assigment_with_smaller_slice_than_iter()
	test_slice_assigment_positive_step()
	test_slice_assigment_negative_step()