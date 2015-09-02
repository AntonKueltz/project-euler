def euler173():
	tiles = 1000000
	max_side = tiles / 4
	count = 0

	for side in range(2, max_side+1):
		total = side * 4
		cur_side = side

		while total <= tiles and cur_side > 1:
			count += 1
			cur_side -= 2
			total += cur_side * 4

	return count

if __name__ == "__main__":
	print euler173()