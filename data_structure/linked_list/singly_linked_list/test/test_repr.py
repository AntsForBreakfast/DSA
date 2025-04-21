import pytest
from linked_list import LinkedList

def test_repr():
	data = [5,6]
	instance = LinkedList(data)
	assert repr(instance) == "LinkedList(Node(value=5, _next=Node(value=6, _next=None)))"

if __name__ == "__main__":
	test_repr()