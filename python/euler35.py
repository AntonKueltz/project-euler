import euler_util
	
def skip(n, scale):
	if scale == 1: return False	# doesn't apply to single digit numbers
	
	# skip a number if it's most sig digit is greater than any other digit
	most_sig = n / scale
	
	for c in str(n % scale):
		if int(c) < most_sig: return True
		
	return False

def euler35():
	"""
	The number, 197, is called a circular prime because all rotations of the
	digits: 197, 971, and 719, are themselves prime.

	There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
	71, 73, 79, and 97.

	How many circular primes are there below one million?
	"""
	primes = euler_util.gen_primes_to(1000000)
	circular = []
	
	for prime in primes:	
		scale = 10**(len(str(prime))-1)
		if skip(prime, scale) or prime in circular: continue
		
		next = ((prime % scale) * 10) + (prime / scale)
		tmp = [prime]
		is_circular = True
		
		while next != prime:
			if next not in primes: 
				is_circular = False
				break
			else: tmp.append(next)
			
			next = ((next % scale) * 10) + (next / scale)
			
		if is_circular: circular += tmp

	return len(circular)

if __name__ == "__main__":
	print euler35() # 26 seconds :/
