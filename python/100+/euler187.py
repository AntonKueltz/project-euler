from euler_util import gen_primes_to

def euler187():
	n = 10**8
	ps = gen_primes_to(n / 2)
	count, i, j = 0, 0, len(ps)-1

	while i <= j:
		while ps[i] * ps[j] >= n: j -= 1
		count += j-i+1
		i += 1

	return count

if __name__ == "__main__":
	print euler187()
