def euler05():
	"""
	2520 is the smallest number that can be divided by each of the numbers
	from 1 to 10 without any remainder.

	What is the smallest positive number that is evenly divisible by all of
	the numbers from 1 to 20?
	"""
	# if a number is not prime only multiply by the factors not already present
	return 1*2*3*2*5*1*7*2*3*1*11*1*13*1*1*2*17*1*19*1
	
if __name__ == "__main__":
	print euler05()
