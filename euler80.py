def root_digit_sum(n):
	if n**0.5 == int(n**0.5): return 0
	
	s, c, p = 0, n, 0

	for i in range(100):
		x = 1
		while x*(20*p + x) <= c: x += 1
		x -= 1
		
		s += x
		y = x*(20*p + x)
		
		
		p = p * 10 + x
		c = (c-y)*100

	return s

def euler80():
	return sum([root_digit_sum(n) for n in range(100)])

if __name__ == "__main__":
	print euler80()