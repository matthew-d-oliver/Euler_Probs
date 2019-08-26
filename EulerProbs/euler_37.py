def isprime(numb):
	num = int(numb)
	for i in range(2,num//2):
		if (num%i)==0 & (num!=4):
			return 0
	return 1


def lefttrunc(numb):
	num=str(numb)
	for i in range(0,len(num)):
		isprime(num[0:-(i-1)])


#print('number biotch:')
#num = input()
#if isprime(num):
#	print ('You got yourself a prime!')
#else:
#	print('nah b she b divisible')
