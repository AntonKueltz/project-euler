from fractions import gcd

def euler75():
	"""
	It turns out that 12 cm is the smallest length of wire that can be bent to
	form an integer sided right angle triangle in exactly one way, but there
	are many more examples.
	
	In contrast, some lengths of wire, like 20 cm, cannot be bent to form an 
	integer sided right angle triangle, and other lengths allow more than one
	solution to be found; for example, using 120 cm it is possible to form
	exactly three different integer sided right angle triangles.
	
	(30, 40, 50), (20, 48, 52), (24, 45, 51)
	
	Given that L is the length of the wire, for how many values of L <= 
	1,500,000 can exactly one integer sided right angle triangle be formed?
	"""
	lengths = [0]*1500001

	# bound at sqrt(max / 2) since L is at least 2 * m**2
	for m in range(2, int((1500000/2)**0.5)): 
		for n in range(1, m):
			
			# pythagorean triples generated by coprimes that aren't both odd
			if not (m - n) & 1 or gcd(m, n) != 1: continue
			
			s = sum([m**2, 2*m*n, m**2])
			next, i = s, 1
			
			while next <= 1500000:
				lengths[next] += 1
				i += 1
				next = s * i
	
	return sum([1 for i in lengths if i == 1])
	
if __name__ == "__main__":
	print euler75()
