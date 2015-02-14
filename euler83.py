def read_in_matrix():
	f = open("p083_matrix.txt", "r")
	rows = f.read().split("\n")
	
	m = []
	for row in rows[:-1]: 
		m.append([[False, 1000000, int(num)] for num in row.split(",")])
	
	return m
	
def get_neighbours(m, row, col):
	# create set of unvisited neighbours
	neighbours = []
	if row > 0 and not m[row-1][col][0]: 
		neighbours.append((row-1, col))
	if row < len(m)-1 and not m[row+1][col][0]: 
		neighbours.append((row+1, col))
	if col > 0 and not m[row][col-1][0]: 
		neighbours.append((row, col-1))
	if col < len(m[0])-1 and not m[row][col+1][0]: 
		neighbours.append((row, col+1))
		
	return neighbours
	
def get_next_node(m):
	best = (1000000, (0, 0))
	
	# get the node with the shortest distance not yet visited
	for r in range(len(m)):
		for c in range(len(m[r])):
			if not m[r][c][0] and m[r][c][1] < best[0]:
				best = (m[r][c][1], (r, c))
				
	return best[1]

def min_path(m):
	# Dijkstra's Algorithm 
	row, col = 0, 0
	m[row][col][1] = m[row][col][2]
	
	while not m[len(m)-1][len(m[0])-1][0]:
		neighbours = get_neighbours(m, row, col)
		
		# find current shortest distance
		dist_to_idx = {}
		for (r, c) in neighbours:
			tmp_dist = m[row][col][1] + m[r][c][2]
			if tmp_dist < m[r][c][1]: m[r][c][1] = tmp_dist
			dist_to_idx[m[r][c][1]] = (r, c)
			
		m[row][col][0] = True # mark as visited
		
		row, col = get_next_node(m)
	
	return m[len(m)-1][len(m[0])-1][1]

def euler83():
	m = read_in_matrix()
	return min_path(m)

if __name__ == "__main__":
	print euler83()
