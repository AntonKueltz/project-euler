def nCr(n, r):
	if r == 0 or n == r: return 1
	
	mul = lambda x,y: x*y
	return reduce(mul, range(r+1, n+1)) / reduce(mul, range(1, (n-r)+1))

def euler53():
	"""
	There are exactly ten ways of selecting three from five. In combinatorics
	we use the notation, 5C3 = 10.
	
	In general nCr = n! / r!(n-r)!
	
	It is not until n = 23 that a value exceeds one-million: 23C10 = 1144066.
	
	How many, not necessarily distinct, values of nCr, for 1 <= n <= 100, are
	greater than one-million?
	"""
	total = 0
	
	for n in range(23, 101):
		for r in range(0, n+1):
			if nCr(n, r) > 1000000:
				total += (n - 2*r + 1)
				break
	
	return total

if __name__ == "__main__":
	print euler53()
