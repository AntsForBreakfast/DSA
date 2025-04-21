from typing import Iterable
from misc.get_data import load_big_data_set

def binary_search(iterable: Iterable, search_string: str) -> tuple[bool, str | None]:
    data = [string.lower().strip() for string in iterable]
    search = search_string.lower()

    left = 0
    right = len(data) - 1

    while right - left > 1:
        midpoint = (left + right) // 2

        if data[midpoint] == search:
            return True, midpoint

        if data[midpoint] <= search:
            left = midpoint - 1
        else:
            right = midpoint + 1

    return False, None
	


def recursive_binary_search(iterable: Iterable, search_string: str) -> tuple[bool, str | None]:
    def search(iterable: Iterable, search_string:str, left:int, right:int) -> tuple[bool, str | None]:
        midpoint = (left + right) // 2

        if iterable[midpoint] == search_string:
            return True, midpoint

        if right - left == 1:
            return False, None

        if iterable[midpoint] <= search_string:
            left = midpoint
        else:
            right = midpoint

        return search(iterable, search_string, left, right)

    data = [string.lower().strip() for string in iterable]
    search_string = search_string.lower()

    left = 0
    right = len(data) - 1
    
    return search(data, search_string, left, right)

x = load_big_data_set()
a = binary_search(x, 'personal')
print(a)