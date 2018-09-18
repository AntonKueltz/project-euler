def fifth_pow_sum(n):
	s = 0
	
	while n > 0:
		s += (n % 10)**5
		n /= 10
		
	return s

def euler30():
	"""
	Surprisingly there are only three numbers that can be written as the sum 	of fourth powers of their digits:

	1634 = 14 + 64 + 34 + 44
	8208 = 84 + 24 + 04 + 84
	9474 = 94 + 44 + 74 + 44
	As 1 = 14 is not a sum it is not included.

	The sum of these numbers is 1634 + 8208 + 9474 = 19316.

	Find the sum of all the numbers that can be written as the sum of fifth 	powers of their digits
	"""
	pow_sum = 0
	
	# upper bound should be lowered to decrease run time
	for n in range(2, 1000000):
		if n == fifth_pow_sum(n): pow_sum += n
		
	return pow_sum

if __name__ == "__main__":
	print euler30()