from fractions import gcd

def euler139():
	limit = 100000000
	m, sm = 1, 0

	while (2*m**2 + 2*m) < limit:
		for n in range((m % 2) + 1, m, 2):
			if gcd(m, n) == 1:
				a = m**2 - n**2
				b = 2*m*n
				c = m**2 + n**2

				if c % abs(b-a) == 0:
					print a, b, c
					sm += (limit / (a+b+c))
		m += 1

	return sm

if __name__ == "__main__":
	print euler139()