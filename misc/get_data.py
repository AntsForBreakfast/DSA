def load_big_data_set() -> list[str]:
	with open('misc\\huge_text.txt', 'r') as f:
		data = [line for line in f]
		return sorted(data)