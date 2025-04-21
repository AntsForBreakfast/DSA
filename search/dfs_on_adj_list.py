from typing import TypedDict

class GraphEdge(TypedDict):
	to: int
	weight: int

type WeightedAdjacencyList = list[list[GraphEdge]]

def walk(
	graph: WeightedAdjacencyList,
	curr: int,
	needle: int,
	seen: list[bool],
	path: list[int]) -> bool:

	if seen[curr]:
		return False

	seen[curr] = True

	# pre
	path.append(curr)
	if curr == needle:
		return True

	# recurse
	lst = graph[curr]
	for i in range(len(lst)):
		edge = lst[i]

		if walk(graph, edge['to'], needle, seen, path):
			return True

	# post
	path.pop()

	return False

def depth_first_search(
	graph:WeightedAdjacencyList,
	source:int,
	needle:int) -> list[int] | None:
	
	seen: list[bool] = [False] * len(graph)
	path: list[int] = []

	walk(graph, source, needle, seen, path)

	if len(path) == 0:
		return None

	return path


graph:WeightedAdjacencyList = [
	[
		{'to': 1, 'weight':1},
		{'to': 3, 'weight': 5},
		{'to': 2, 'weight':4}
	],
	[],
	[{'to': 3, 'weight':2}],
	[{'to': 4, 'weight':5}],
	[],
]

path = depth_first_search(graph, 0, 4)
