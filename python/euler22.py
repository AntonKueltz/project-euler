def build_names():
	f = open("names.txt")
	names = f.read().replace("\"", "")
	sorted_list = sorted(names.split(","))
	return sorted_list
	
def euler22():
	"""
	Using names.txt (right click and 'Save Link/Target As...'), a 46K text
	file containing over five-thousand first names, begin by sorting it into
	alphabetical order. Then working out the alphabetical value for each name,
	multiply this value by its alphabetical position in the list to obtain a
	name score.

	For example, when the list is sorted into alphabetical order, COLIN, which
	is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
	COLIN would obtain a score of 938 x 53 = 49714.

	What is the total of all the name scores in the file?
	"""
	name_score = 0
	names_list = build_names()
	offset = 64	# "A" is equivalent to 65
	
	for i in range(0, len(names_list)):
		name_val = sum([(ord(c) - offset) for c in names_list[i]])
		name_score += ((i+1) * name_val)
	
	return name_score

if __name__ == "__main__":
	print euler22()
