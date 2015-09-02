partitions = [1]
pents = []

def gen_ps(n):
	gen_pent = lambda m: int(0.5 * m * (3*m - 1))
	p, idx = 0, 0
	
	try: 
		pent = pents[idx]
	except: 
		pent = gen_pent(1)
		pents.append(pent)
	
	while pent <= n:
		if idx % 4 in [0, 1]: p += partitions[n - pent]
		else: p -= partitions[n - pent]
		
		idx += 1
		try:
			pent = pents[idx]
		except:
			seed = (idx / 2) + 1
			if idx % 2:
				pent = gen_pent(-seed)
				pents.append(pent)
			else:
				pent = gen_pent(seed)
				pents.append(pent)

	partitions.append(p)
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
