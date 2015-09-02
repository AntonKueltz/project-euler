from euler_util import gen_primes_to

def euler214():
	n = 40000000
	ps = gen_primes_to(n)
	ts = range(n)
	ls = [0]*n
	s = 0

	# calculate totients
	for p in ps:
		for r in range(p, n, p):
			ts[r] = int(ts[r] * (1.0 - 1.0 / p))

	ls[1] = 1
	for i in range(2, len(ls)):
		ls[i] = ls[ts[i]] + 1

		# if prime chain is 25
		if ts[i] == i-1 and ls[i] == 25: s += i

	return s

if __name__ == "__main__":
	print euler214()
