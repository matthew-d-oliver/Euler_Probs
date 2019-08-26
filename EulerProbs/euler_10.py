def isprime(numb):
	num = int(numb)
	for i in range(2,num//2):
		if (num%i)==0:
			return 0
	return 1
sumr=0
for j in range(3,2000000,2):
	if isprime(j)!=0:
		sumr +=j
print(sumr+2)