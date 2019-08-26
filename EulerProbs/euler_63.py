'''The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?'''
#Euler problem 63 Matt Oliver

county = 0
listy = []
for i in range(1,100):
	for j in range(1,100):
		num = i**j
		if len(str(num)) ==j:
			listy.append(str(num)+ '=' +str(i)+'*'+ str(j))

			county += 1

print(listy)
print(str(county))
