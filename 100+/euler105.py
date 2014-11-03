from itertools import combinations

def get_sets():
	f = open("p105_sets.txt", 'r')
	sets = [map(int, line.split(",")) for line in f.read().split("\n")]
	f.close()
	return sets

def check_properties(s):
	l = len(s)
	indices = "0123456789ABCDEF"[:l]
	hex_to_int = {
		"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, 
		"8": 8, "9": 9, "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15
	}

	for i in range(1, l+1):
		subset_sums = []

		# go through all subsets of length i
		for index in ["".join(c) for c in combinations(indices, i)]:
			sm1 = sum([s[hex_to_int[idx]] for idx in index])

			# condition i
			if sm1 in subset_sums: return False
			else: subset_sums.append(sm1)

			remaining = "".join([ri for ri in indices if ri not in index])
			# go through all subsets of the remaining elements
			for j in range(i+1, l+1):
				for index2 in ["".join(c2) for c2 in combinations(remaining, j)]:
					sm2 = sum([s[hex_to_int[idx2]] for idx2 in index2])

					# condition i & ii
					if sm2 <= sm1: return False

	return True

def euler105():
	sm = 0
	sets = get_sets()

	for s in sets:
		if check_properties(s):
			sm += sum(s)

	return sm
	
if __name__ == "__main__":
	print euler105() 