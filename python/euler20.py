def euler20():
	"""
	n! means n x (n - 1) x ... x 3 x 2 x 1

	For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
	and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 =
	27.

	Find the sum of the digits in the number 100!
	"""
	mul = lambda x, y: x*y
	return sum([int(c) for c in str(reduce(mul, range(1, 101)))])

if __name__ == "__main__":
	print euler20()
