import pytest
from linked_list import Node

def test_node_equal_node():
	node1 = Node(value=1, _next=Node(value=2, _next=None))
	node2 = Node(value=1, _next=Node(value=2, _next=None))
	assert node1 == node2

def test_node_not_equal_node():
	node1 = Node(value=1, _next=Node(value=2, _next=None))
	node2 = Node(value=1, _next=None)
	assert node1 != node2

def test_node_values_equal():
	node1 = Node(value='a', _next=None)
	node2 = Node(value='a', _next=None)
	assert node1.value == node2.value

def test_node_values_not_equal():
	node1 = Node(value='a', _next=None)
	node2 = Node(value='b', _next=None)
	assert node1.value != node2.value

		
if __name__ == "__main__":
	test_node_not_equal_node()
	test_node_equal_node()
	test_node_values_equal()
	test_node_values_not_equal()
	test_node_length_equal()
	test_node_length_equal()