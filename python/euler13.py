def euler13():
	"""
	Work out the first ten digits of the sum of the following one-hundred 50
	digit numbers [in nums.txt].
	"""
	f = open("nums13.txt")
	nums = [int(line) for line in f.read().split()]
	return sum(nums) / (10 ** (len(str(sum(nums))) - 10))
	
if __name__ == "__main__":
	print euler13()
