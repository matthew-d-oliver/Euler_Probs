def isprime(numb):
	num = int(numb)
	for i in range(2,num//2):
		if (num%i)==0:
			return 0
	return 1
j=0
count = 1
while j!=10002:
	count +=1
	if isprime(count) == 1:
		j +=1


print (count)
print(j)



