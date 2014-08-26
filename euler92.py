def dig_sqr_sum(n):
	s = 0
	
	while n > 0:
		s += (n % 10)**2
		n /= 10
		
	return s

def euler91():
	"""
	A number chain is created by continuously adding the square of the digits
	in a number to form a new number until it has been seen before.
	
	Any chain that arrives at 1 or 89 will become stuck in an endless loop.
	What is most amazing is that EVERY starting number will eventually arrive
	at 1 or 89.
	
	How many starting numbers below ten million will arrive at 89?
	"""
	arrives_at_eightynine = [False]*10000000
	visited = [False]*10000000
	
	for i in range(1, 10000000):
		if visited[i]: continue
		
		next = i
		chain = [next]
		end_result = False
	
		while True:
			if next == 1: 
				end_result = False
				break
			if next == 89:
				end_result = True
				break
				
			next = dig_sqr_sum(next)
			
			if visited[next]:
				end_result = arrives_at_eightynine[next]
				break
			
			chain.append(next)
			
		for val in chain:
			visited[val] = True
			arrives_at_eightynine[val] = end_result
				
	return sum([1 for b in arrives_at_eightynine if b])	 
	
if __name__ == "__main__":
	print euler91()
