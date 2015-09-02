def modexp(base, exp, mod):
	neg = base < 0
	base = base % mod
	res = 1
	
	while exp > 0:
		if exp % 2 == 1:
			res = (res * base) % mod
		exp = exp >> 1
		base = (base * base) % mod
	
	if neg: return res - mod
	else: return res

def euler188():
	a = 1777
	k = 1855
	m = 10**8
	# totient of 10^8, the modulo to get the last 8 digits
	t = int(m * (1.0 - (1.0/5.0)) * (1.0 - (1.0/2.0)))

	for _ in range(k-2):
		a = modexp(1777, a, t)
	
	return modexp(1777, a, m)

if __name__ == "__main__":
	print euler188()
