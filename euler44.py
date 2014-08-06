def euler44():
	"""
	Pentagonal numbers are generated by the formula, Pn=n(3n-1)/2. The first
	ten pentagonal numbers are:

	1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

	It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their
	difference, 70 - 22 = 48, is not pentagonal.

	Find the pair of pentagonal numbers, Pj and Pk, for which their sum and
	difference are pentagonal and D = |Pk - Pj| is minimised; what is the
	value of D?
	"""
	pents = [1]
	seed = 2
	gen_pent = lambda n: (n * (3 * n - 1)) / 2
	valid_pent = lambda x: ((24 * x + 1)**0.5) % 6 == 5

	while True:
		new = gen_pent(seed)
		pents.append(new)
		
		for i in range(0, len(pents)-1)[::-1]: # backwards
			tmp = pents[i]
			
			if valid_pent(new + tmp) and valid_pent(new - tmp):
				return new - tmp
				
		seed += 1
				
if __name__ == "__main__":
	print euler44()
	
