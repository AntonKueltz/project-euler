test = [[131, 673, 234, 103, 18],
		[201, 96, 342, 965, 150],
		[630, 803, 746, 422, 111],
		[537, 699, 497, 121, 956],
		[805, 732, 524, 37, 331]]

def read_in_matrix():
	f = open("p082_matrix.txt", "r")
	rows = f.read().split("\n")
	
	m = []
	for row in rows[:-1]: m.append(map(int, row.split(",")))
	
	return m

def min_path(m):
	# work our way over by column
	for col in range(1, len(m[0])):
	
		# make columns easier to work with
		col_vals = []
		for row in range(len(m)): col_vals.append(m[row][col])
		
		for row in range(len(m)):
			# top row case
			if row != 0: best = min(m[row][col-1], m[row-1][col])
			else: best = m[row][col-1]
			
			# see if any path from a lower row is better
			for lower in range(row+1, len(m)):
				if sum(col_vals[row+1:lower+1]) >= best: break
				else: 
					dist = m[lower][col-1] + sum(col_vals[row+1:lower+1])
					if dist < best: best = dist
		
			m[row][col] += best
			
	last_col = []
	for row in range(len(m)): last_col.append(m[row][len(m[0])-1])
	
	return min(last_col) 

def euler82():
	m = read_in_matrix()
	return min_path(m)

if __name__ == "__main__":
	print euler82()
