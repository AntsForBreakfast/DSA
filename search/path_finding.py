"""Recursive path finding algorithm used on Simple Maze Solver"""

directions = (
	(-1, 0), # Top
	(1, 0), # Bottom
	(0, -1), # Left
	(0,1) # Right
	)

def walk(
	maze: list[str],
	wall: str,
	current_pos: tuple[int,int],
	end_pos: tuple[int,int],
	seen: list[list[bool]],
	path: list[tuple[int,int]]
) -> bool:

	curr_x, curr_y = current_pos
	end_x, end_y = end_pos
	
	# off the map
	outside_row = curr_x < 0 or curr_x >= len(maze[0])
	outside_column = curr_y < 0 or curr_y >= len(maze)

	if outside_row or outside_column:
	    return False

	# on a wall
	if maze[curr_y][curr_x] == wall:
		return False

	# the end
	if curr_x == end_x and curr_y == end_y:
		path.append(end)
		return True

	# has seen
	if seen[curr_y][curr_x]:
		return False

	# 3 recurse
	# pre-recursion
	seen[curr_y][curr_x] = True
	path.append(current_pos)

	# recurion
	for i in range(len(directions)):
		if walk(
			maze=maze,
			wall=wall,
			current_pos=(
				curr_x + directions[i][0],
				curr_y + directions[i][1],
			),
			end_pos=end_pos,
			seen=seen,
			path=path
		):
			return True

	# post-recursion
	path.pop()

	return False

def solve(
	maze: list[str],
	wall: str,
	start: tuple[int,int],
	end: tuple[int,int]
):
	seen: list[list[bool]] = []
	path: list[tuple[int,int]] = []

	for i in range(len(maze)):
		seen.append([False] * len(maze[i]))

	walk(
		maze=maze,
		wall=wall,
		current_pos=start,
		end_pos=end,
		seen=seen,
		path=path
	)

	return path


maze = [
	"XXXXXXXXXX X",
	"X        X X",
	"X        X X",
	"X XXXXXXXX X",
	"X          X",
	"X XXXXXXXXXX",
]
wall = 'X'
start = (10, 0)
end = (1, 5)

result = solve(maze, wall, start, end)
from pprint import pprint
pprint(result)