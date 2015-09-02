def euler39():
	"""
	If p is the perimeter of a right angle triangle with integral length
	sides, {a,b,c}, there are exactly three solutions for p = 120.

	{20,48,52}, {24,45,51}, {30,40,50}

	For which value of p <= 1000, is the number of solutions maximised?
	"""
	count = [0] * 1001

	for a in range(1, 333):
		for b in range(a+1, 500):
			c = (a**2 + b**2) ** 0.5
			p = a + b + int(c)
			
			if int(c) != c: continue
			if p > 1000: break
			
			count[p] += 1
			
	return count.index(max(count))

if __name__ == "__main__":
	print euler39()
