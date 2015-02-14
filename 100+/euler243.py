import euler_util

def totients(primes):
	totients = range(primes[-1])
	
	for p in primes:
		idx = 1
		while idx * p < primes[-1]:
			totients[idx*p] *= (1.0 - 1.0 / p)
			idx += 1		
	
	return totients

def starting_point(limit):
	primes = euler_util.gen_primes_to(100)
	idx = 0
	top, bottom = 1, 1
	
	# fast upper bound since phi(prime) = prime - 1
	while float(top) / float(bottom) > limit:
		idx += 1
		bottom = reduce(lambda x,y: x*y, primes[:idx]) - 1
		top = reduce(lambda x,y: x*y, [p-1 for p in primes[:idx]])
		
	# starting point is the product of all primes before the upper bound
	d = reduce(lambda x,y: x*y, primes[:idx-1])
	phi_d = reduce(lambda x,y: x*y, [p-1 for p in primes[:idx-1]])
	return d, phi_d

def euler243():
	# resilient fractions of n = numbers < n coprime to n = phi(n) (eulers totient)
	lower_limit = 15499.0 / 94744.0
	d, phi_d = starting_point(lower_limit)

	# generate totients for composites
	primes = euler_util.gen_primes_to(100)	
	phi = totients(primes)
	
	# multiply the starting point by increasing composites
	for i in range(4, 100):
		if i in primes: continue
		
		new_d = i * d
		new_phi_d = phi[i] * phi_d
		
		if new_phi_d / (new_d-1) < lower_limit: return new_d
		
		
if __name__ == "__main__":
	print euler243()
