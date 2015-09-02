def euler15():
	"""
	Starting in the top left corner of a 2x2 grid, and only being able to move
	to the right and down, there are exactly 6 routes to the bottom right
	corner.


	How many such routes are there through a 20x20 grid?
	"""
	# 40 (20+20) choose 20 (the middle)
	mul = lambda x, y: x*y
	return reduce(mul, range(1, 41)) / (reduce(mul, range(1, 21)))**2

if __name__ == "__main__":
	print euler15()
