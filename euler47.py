prime_factors = [[]]*1000000

def distinct_prime_facs(n):
	working_list = []
	for i in range(2, int(n**0.5)+1):
		if n % i == 0:
			working_list += prime_factors[n / i]
			working_list.append(i)
			prime_factors[n] = list(set(working_list))
			return len(prime_factors[n])
			
	prime_factors[n] = [n]
	return 1

def euler47():
	"""
	The first two consecutive numbers to have two distinct prime factors are:
	
	14 = 2x7
	15 = 3x5
	
	The first three consecutive numbers to have three distinct prime factors are:
	
	644 = 2^2x7x23
	645 = 3x5x43
	646 = 2x17x19
	
	Find the first four consecutive numbers to have four distinct prime factors.
	What is the first of these numbers?
	"""
	i = 1
	consec = 0
	
	while True:
		facs = distinct_prime_facs(i)
		
		if facs == 4: consec += 1
		else: consec = 0
		
		if consec == 4: return i - 3
		
		i += 1
	
if __name__ == "__main__":
	print euler47()
