def euler138():
	"""
	Once again check out http://www.alpertron.com.ar/QUAD.HTM for
	where the magic vals come from once you have pell's equation
	"""
	x, y = 0, -1
	p, q, k, r, s, l = -9, -4, 4, -20, -9, 8
	sm = 0

	for _ in range(12):
		x_n1 = p*x + q*y + k
		y_n1 = r*x + s*y + l

		x = x_n1
		y = y_n1

		sm += abs(y)

	return sm

if __name__ == "__main__":
	print euler138()