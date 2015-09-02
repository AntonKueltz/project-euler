from euler_util import gen_primes_to

def egcd(a, b):
	if a == 0: return (b, 0, 1)
	else:
		g, y, x = egcd(b % a, a)
		return (g, x-(b // a)*y, y)

def modinv(a, mod):
	gcd, x, y = egcd(a, mod)
	if gcd != 1: return None
	else: return x % mod

def S(p):
	v1 = modinv(p-2, p)
	v2 = (v1*modinv(p-3, p)) % p 
	v3 = (v2*modinv(p-4, p)) % p
	return (v1+v2+v3) % p

def euler381():
	ps = gen_primes_to(10**8)
	total = 0

	for p in ps:
		if p > 5: total += S(p)
		elif p == 5: total += 4

	return total

if __name__ == "__main__":
	print euler381()