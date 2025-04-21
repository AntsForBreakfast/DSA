import pytest
from linked_list import Node

def test_node_not_node():
	node1 = Node(value='a', _next=None)
	assert node1.__eq__(1) is NotImplemented

if __name__ == "__main__":
	test_node_not_node()