def euler97():
	"""
	In 2004 there was found a massive non-Marsenne prime which contains
	2,357,207 digits: 28433 x 2^7830457 + 1. Find the last ten digits of this
	prime number.
	"""
	return (28433 * 2**7830457 + 1) % 10**10

if __name__ == "__main__":
	print euler97()
