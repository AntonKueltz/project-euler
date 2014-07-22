def euler28():
	"""
	Starting with the number 1 and moving to the right in a clockwise
	direction a 5 by 5 spiral is formed as follows:

	21 22 23 24 25
	20  7  8  9 10
	19  6  1  2 11
	18  5  4  3 12
	17 16 15 14 13

	It can be verified that the sum of the numbers on the diagonals is 101.

	What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
	formed in the same way
	"""
	spiral_sum = 1
	gap = 2
	last_val = 1
	
	while gap < 1001:
		spiral_sum += last_val*4 + gap*10
		last_val += gap*4
		gap += 2
		
	return spiral_sum

if __name__ == "__main__":
	print euler28()
