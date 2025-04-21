import pytest
from linked_list import LinkedList

def test_len():
	data = [1,2,3,4,5]
	instance = LinkedList(data)
	assert len(instance) == 5

if __name__ == "__main__":
	test_len()