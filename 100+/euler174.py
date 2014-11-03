def euler174():
	tiles = 1000000
	counts = [0]*1000001
	max_side = tiles / 4
	count = 0

	for side in range(2, max_side+1):
		total = side * 4
		cur_side = side

		while total <= tiles and cur_side > 1:
			counts[total] += 1
			cur_side -= 2
			total += cur_side * 4

	return sum([1 for count in counts if (1 <= count and count <= 10)])

if __name__ == "__main__":
	print euler174()