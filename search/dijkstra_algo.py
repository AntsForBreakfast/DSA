from typing import TypedDict

class GraphEdge(TypedDict):
	to: int
	weight: int

type WeightedAdjacencyList = list[list[GraphEdge]]

def has_unvisited(seen: list[bool], dists: list[float]) -> bool:
	return any(not s and d < float('inf') for s, d in zip(seen, dists))

def get_lowest_unvisited(seen: list[bool], dists: list[float]) -> int:
	idx = -1
	lowest_distance = float('inf')

	for i in range(len(seen)):
		if seen[i]:
			continue

		if lowest_distance > dists[i]:
			lowest_distance = dists[i]
			idx = i

	return idx

def dijkstra(
	arr:WeightedAdjacencyList,
	source:int,
	sink:int) -> list[int] | None:
	
	seen: list[bool] = [False]*len(arr)
	prev: list[int] = [-1]*len(arr)
	dists: list[float] = [float('inf')]*len(arr)
	dists[source] = 0

	while has_unvisited(seen, dists):
		curr = get_lowest_unvisited(seen, dists)
		seen[curr] = True

		adjs = arr[curr]
		for i in range(len(adjs)):
			to, weight = adjs[i].values()

			if seen[to]:
				continue

			dist = dists[curr] + weight
			if dist < dists[to]:
				dists[to] = dist
				prev[to] = curr

	out: list[int] = []
	curr = sink

	while prev[curr] != -1:
		out.append(curr)
		curr = prev[curr]

	out.append(source)
	out.reverse()
	return out

graph:WeightedAdjacencyList = [
	[
		{'to': 1, 'weight': 4},
		{'to': 2, 'weight': 2},
	],
	[
		{'to': 3, 'weight': 2},
		{'to': 4, 'weight': 3},
		{'to': 2, 'weight': 3},
	],
	[
		{'to': 1, 'weight': 1},
		{'to': 4, 'weight': 5},
	],
	[],
	[
		{'to': 3, 'weight': 1},
	],
]

path = dijkstra(graph, 0, 4)
print(path)