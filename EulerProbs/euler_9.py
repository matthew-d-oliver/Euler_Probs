for i in range(3,1000):
	for j in range(4,999):
		ksquared = i**2 + j**2
		k = ksquared **.5

		if i + j + k ==1000:
			print(i*j*k)
			break

#I CHEATED ON THIS ONE