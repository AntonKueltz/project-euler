def euler48():
	"""
	The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

	Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
	"""
	last_ten = 0
	
	for i in range(1, 1001):
		last_ten = (last_ten + i**i) % 10**10
		
	return last_ten

if __name__ == "__main__":
	print euler48()
