def gen_4dig_primes():
	primes = [2]
	dig4_primes = []
	i = 3
	
	while i < 10000:
		p_index = 0
		is_prime = True
		
		while primes[p_index] <= i**0.5:
			if i % primes[p_index] == 0: 
				is_prime = False
				break
			p_index += 1
		 
		if is_prime:
			primes.append(i)
			if i > 999: dig4_primes.append(i)
			
		i += 2
			
	return dig4_primes
		
def euler49():
	"""
	The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
	increases by 3330, is unusual in two ways: (i) each of the three terms are
	prime, and, (ii) each of the 4-digit numbers are permutations of one
	another.

	There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
	primes, exhibiting this property, but there is one other 4-digit
	increasing sequence.

	What 12-digit number do you form by concatenating the three terms in this
	sequence?
	"""
	cands = gen_4dig_primes()
	sequences = []
	
	for i in range(0, len(cands)):
		for j in range(i+1, len(cands)):
			if set(str(cands[i])) == set(str(cands[j])):
				diff = cands[j] - cands[i]
				third = cands[j] + diff
				
				if third in cands and set(str(third)) == set(str(cands[i])):
					sequences.append(str(cands[i])+str(cands[j])+str(third))
					
	return sequences

if __name__ == "__main__":
	print euler49()
