def euler74():
	"""
	The number 145 is well known for the property that the sum of the factorial
	of its digits is equal to 145.
	
	Perhaps less well known is 169, in that it produces the longest chain of 
	numbers that link back to 169; it turns out there are only three such
	loops that exist:
	
	169 -> 363601 -> 1454 -> 169
	871 -> 45361 -> 871
	872 -> 45362 -> 872
	
	How many chains, with a starting number below one million, contain exactly
	sixty non-repeating terms?
	"""
	mul = lambda x,y: x*y
	fac = lambda n: 1 if n in (0,1) else reduce(mul, range(1, n+1))
	dig_fac_sum = lambda n: sum(map(fac, [int(c) for c in str(n)]))
	total = 0
	chains = [0]*1000001
	
	for start in range(2, 1000000):
		chain_len = 1
		next_val = dig_fac_sum(start)
		
		while True:
			chain_len += 1
		
			if next_val in [871, 872, 45361, 45362]:
				chain_len += 1
				break
			if next_val in [169, 1454, 363601]:
				chain_len += 2
				break
				
			prev_val = next_val
			next_val = dig_fac_sum(next_val)
			
			if next_val < start:
				chain_len += chains[next_val]
				break
				
			if prev_val == next_val: break
			
		if chain_len == 60: total += 1
		chains[start] = chain_len

	return total

if __name__ == "__main__":
	print euler74()
