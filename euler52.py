def euler52():
	"""
	It can be seen that the number, 125874, and its double, 251748, contain exactly
	the same digits, but in a different order.

	Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
	contain the same digits.
	"""
	x = 0
	while True:
		x += 1
		if sorted(str(x)) != sorted(str(2*x)): continue
		if sorted(str(x)) != sorted(str(3*x)): continue
		if sorted(str(x)) != sorted(str(4*x)): continue
		if sorted(str(x)) != sorted(str(5*x)): continue
		if sorted(str(x)) != sorted(str(6*x)): continue
		return x

if __name__ == "__main__":
	print euler52()
