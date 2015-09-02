def euler18():
	"""
	By starting at the top of the triangle below and moving to adjacent
	numbers on the row below, the maximum total from top to bottom is 23.

	3
	7 4
	2 4 6
	8 5 9 3

	That is, 3 + 7 + 4 + 9 = 23.

	Find the maximum total from top to bottom of the triangle below [in 
	pyr18.txt]:
	"""
	f = open("pyr18.txt")
	rows = f.read().split("\n")
	pyramid = []
	for row in rows[:-1]: pyramid.append([int(val) for val in row.split(" ")])
	
	# start on second to last row and work up
	for r in range(len(pyramid)-2, -1, -1):
		for c in range(0, len(pyramid[r])):
			pyramid[r][c] += max(pyramid[r+1][c], pyramid[r+1][c+1])
			
	return pyramid[0][0]
	
if __name__ == "__main__":
	print euler18()
