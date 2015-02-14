from itertools import permutations

def check_vals(vals):
	row1 = vals[0] + vals[5] + vals[6]
	row2 = vals[1] + vals[6] + vals[7]
	row3 = vals[2] + vals[7] + vals[8]
	row4 = vals[3] + vals[8] + vals[9]
	row5 = vals[4] + vals[9] + vals[5]
	
	return row1 == row2 == row3 == row4 == row5
	
def make_sol(cand, vals):
	row1 = cand[0] + cand[5] + cand[6]
	row2 = cand[1] + cand[6] + cand[7]
	row3 = cand[2] + cand[7] + cand[8]
	row4 = cand[3] + cand[8] + cand[9]
	row5 = cand[4] + cand[9] + cand[5]
	
	if(vals.index(min(vals[:5])) == 0):
		return row1 + row2 + row3 + row4 + row5
	elif(vals.index(min(vals[:5])) == 1):
		return row2 + row3 + row4 + row5 + row1
	elif(vals.index(min(vals[:5])) == 2):
		return row3 + row4 + row5 + row1 + row2
	elif(vals.index(min(vals[:5])) == 3):
		return row4 + row5 + row1 + row2 + row3
	else:
		return row5 + row1 + row2 + row3 + row4

def euler68():
	"""
	Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and
	each line adding to nine.

	Working clockwise, and starting from the group of three with the numerically
	lowest external node (4,3,2 in this example), each solution can be described
	uniquely. For example, the above solution can be described by the set: 4,3,2;
	6,2,1; 5,1,3.

	It is possible to complete the ring with four different totals: 9, 10, 11, and
	12. There are eight solutions in total.

	Total	Solution Set
	9	4,2,3; 5,3,1; 6,1,2
	9	4,3,2; 6,2,1; 5,1,3
	10	2,3,5; 4,5,1; 6,1,3
	10	2,5,3; 6,3,1; 4,1,5
	11	1,4,6; 3,6,2; 5,2,4
	11	1,6,4; 5,4,2; 3,2,6
	12	1,5,6; 2,6,4; 3,4,5
	12	1,6,5; 3,5,4; 2,4,6

	By concatenating each group it is possible to form 9-digit strings; the
	maximum string for a 3-gon ring is 432621513.

	Using the numbers 1 to 10, and depending on arrangements, it is possible to
	form 16- and 17-digit strings. What is the maximum 16-digit string for a
	"magic" 5-gon ring?
	"""
	cands = ["".join(p) for p in permutations("0123456789")]
	solutions = []
	
	for cand in cands:
		vals = [int(c)+1 for c in cand]
		if check_vals(vals):
			sol= make_sol(map(str, vals), vals)
			if len(sol) == 16: solutions.append(sol)

	return max(map(int, solutions))

if __name__ == "__main__":
	print euler68()
