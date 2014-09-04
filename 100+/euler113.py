# non bouncy array (sorted by starting digit), (ascending, descending)

def non_bouncy_under_1000():
	non_bouncy = ([0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0])
	
	for i in range(100, 1000):
		first = i % 10
		second = (i / 10) % 10
		third = i / 100
		
		if not (first == second == third):
			if first <= second <= third: 
				non_bouncy[0][third-1] += 1
			if first >= second >= third:
				non_bouncy[1][third-1] += 1
			
	return non_bouncy
	
def update_ascend(first_dig, non_bouncy):
	non_bouncy[0][first_dig-1] += sum(non_bouncy[0][first_dig-1:])
	
def update_descend(first_dig, non_bouncy):
	non_bouncy[1][first_dig-1] += sum(non_bouncy[1][:first_dig])		

# brute force under 987048
def euler113():
	non_bouncy = non_bouncy_under_1000()
	same_and_zero = 9
	
	for length in range(4,6):
		same_and_zero += 18
		for i in range(1, 10):
			update_ascend(i, non_bouncy)
		for i in range(9, 0, -1):
			update_descend(i, non_bouncy)
	
	return sum(non_bouncy[0]) + sum(non_bouncy[1]) + same_and_zero

if __name__ == "__main__":
	print euler113()
