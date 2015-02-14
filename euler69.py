import euler_util

def gen_totients(n):
	totients = range(n+1)
	primes = euler_util.gen_primes_to(n+1)
		
	for p in primes:
		scale = 1
		idx = p
		while idx <= n:
			totients[idx] *= (1.0 - 1.0 / p)
			scale += 1
			idx = scale * p
					
	return totients

def euler69():
	"""
	Euler's totient function phi(n), is used to determine the number of numbers
	less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7,
	and 8, are all less than nine and relatively prime to nine, phi(9)=6.
	
	Find the value of n <= 1000000 for which n/phi(n) is a maximum.
	"""
	n = 1000000
	max_ratio = 0.0, 0
	phi_n = gen_totients(n)
	
	for n in range(2, n+1):
		ratio = n / phi_n[n]
		if ratio > max_ratio[0]: max_ratio = ratio, n
		
	return max_ratio[1]

if __name__ == "__main__":
	print euler69()
