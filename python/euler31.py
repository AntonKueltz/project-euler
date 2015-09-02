def euler31():
	"""
	In England the currency is made up of Pound and pence, and there are eight
	coins in general circulation.
	
	1p, 2p, 5p, 10p, 20p, 50p, 1P (100p), 2P (200p)
	
	It is possible to make 2P the following way:
	
	1x1P + 1x50p + 2x20p + 1x5p + 1+2p + 3x1p
	
	How many different ways can 2P be using any number of coins?
	"""
	sums = [0]*201
	sums[0] = 1
	coins = [1,2,5,10,20,50,100,200]
	
	for c in coins:
		for i in range(c, 201):
			sums[i] += sums[i - c]
					
	return sums[200]

if __name__ == "__main__":
	print euler31()
