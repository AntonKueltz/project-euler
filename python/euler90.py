from itertools import combinations

def all_squares(cube1, cube2):
	first = [0,0,0,1,2,3,4,6,8]
	second = [1,4,9,6,5,6,9,4,1]
	
	if 6 in cube1 and not 9 in cube1: cube1.append(9)
	elif 9 in cube1 and not 6 in cube1: cube1.append(6)
	
	if 6 in cube2 and not 9 in cube2: cube2.append(9)
	elif 9 in cube2 and not 6 in cube2: cube2.append(6)
	
	for i in range(9):
		way1 = (first[i] in cube1 and second[i] in cube2)
		way2 = (first[i] in cube2 and second[i] in cube1)
		if not (way1 or way2): return False
		
	return True

def euler90():
	"""
	Each of the six faces on a cube has a different digit (0 to 9) written on it;
	the same is done to a second cube. By placing the two cubes side-by-side in
	different positions we can form a variety of 2-digit numbers.

	For example, the square number 64 could be formed:

	In fact, by carefully choosing the digits on both cubes it is possible to
	display all of the square numbers below one-hundred: 01, 04, 09, 16, 25, 36,
	49, 64, and 81.

	For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on
	one cube and {1, 2, 3, 4, 8, 9} on the other cube.

	However, for this problem we shall allow the 6 or 9 to be turned upside-down
	so that an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows
	for all nine square numbers to be displayed; otherwise it would be impossible
	to obtain 09.

	In determining a distinct arrangement we are interested in the digits on each
	cube, not the order.

	{1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
	{1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}

	But because we are allowing 6 and 9 to be reversed, the two distinct sets in
	the last example both represent the extended set {1, 2, 3, 4, 5, 6, 9} for the
	purpose of forming 2-digit numbers.

	How many distinct arrangements of the two cubes allow for all of the square
	numbers to be displayed?
	"""
	cubes = [map(int, c) for c in combinations("0123456789", 6)]
	print cubes[:20]
	arrangements = 0
	
	for cube1 in cubes:
		for cube2 in cubes:
			if all_squares(cube1, cube2): arrangements += 1
		
	# order of cubes doesn't matter
	return arrangements / 2

if __name__ == "__main__":
	print euler90()
