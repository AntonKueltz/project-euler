pents = [1]

def gen_ps(n):
	gen_pent = lambda m: int(0.5 * m * (3*m - 1))
	p = 0
	
	idx = 1
	while gen_pent(idx) <= n:
		if idx % 2: p += pents[n - gen_pent(idx)]
		else: p -= pents[n - gen_pent(idx)]
		
		if idx < 0:  idx = abs(idx)+1
		else: idx = -idx

	pents.append(p)
	return p

def euler78():
	"""
	Let p(n) represent the number of different ways in which n coins can be
	separated into piles. For example, five coins can separated into piles in
	exactly seven different ways, so p(5)=7.

	OOOOO
	OOOO   O
	OOO   OO
	OOO   O   O
	OO   OO   O
	OO   O   O   O
	O   O   O   O   O
	Find the least value of n for which p(n) is divisible by one million.
	"""
	n = 1
	
	while gen_ps(n) % 1000000 != 0:
		n += 1
		
	return n
	
if __name__ == "__main__":
	print euler78()
