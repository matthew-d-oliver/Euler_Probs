def num_divs(numb):
	countr = 1
	l = int(numb)
	for i in range(1,int(l**.5)):
		if l%i==0: countr+=2
	return countr
#
#print('gimme a num')
#num= input()
#print(num_divs(num))
y=1
for x in range(2,100000):
	bleh = num_divs(y)
	if bleh>=500:break
	if bleh>=100:
		print(bleh)
		print(y)
	y+=x

print(y)

