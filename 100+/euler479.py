m = 1000000007

# modular exponentiation
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

# extended gcd	
def egcd(a, b):
	if a == 0: return (b, 0, 1)
	else:
		g, y, x = egcd(b % a, a)
		return (g, x-(b // a)*y, y)

# modular inverse using extended gcd
def modinv(a, mod):
	gcd, x, y = egcd(a, mod)
	if gcd != 1: return None
	else: return x % mod
	
def euler479(*args):
	base, gap = 0, -3
	n, s = 10**6, 0
	
	for i in range(1, n+1):
		tmp = (base - modexp(base, n+1, m)) *  modinv(1-base, m)
		s = (s + tmp) % m
		
		base += gap
		gap += -2
    	
	return s % m

if __name__ == "__main__":
	print euler479()
