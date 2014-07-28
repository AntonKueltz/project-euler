def euler04():
	"""
	A palindromic number reads the same both ways. The largest palindrome made
	from the product of two 2-digit numbers is 9009 = 91 x 99.

	Find the largest palindrome made from the product of two 3-digit numbers.
	"""
	largest = 0
	
	for i in range(100, 1000):
		for j in range(i, 1000):
			if str(i*j) == str(i*j)[::-1] and i*j > largest:
				largest = i*j
			
	return largest
	
if __name__ == "__main__":
	print euler04()
