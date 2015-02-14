def nCr(n, r):
	mul = lambda x,y: x*y
	return reduce(mul, range(n-r+1, n+1)) / reduce(mul, range(1, r+1))

def euler85():
	"""
	By counting carefully it can be seen that a rectangular grid measuring
	3 by 2 contains eighteen rectangles.
	
	Although there exists no rectangular grid that contains two million
	rectangles, find the area of the grid with the nearest solution.
	"""
	height = 2
	width = 1
	closest = 2000000, 0
	
	while nCr(height+1,2) <= 2000000:
		width = 1
		while True:
			poss_recs = nCr(height+1, 2) * nCr(width+1, 2)
			if poss_recs > 2000000 + closest[1]: break
			
			diff = abs(2000000 - poss_recs)
			if diff < closest[0]: closest = diff, (width * height)
			
			width += 1	
		
		height += 1
		
	return closest[1]

if __name__ == "__main__":
	print euler85()
