
def check_bin(binar): #checks if binary version of number is palindrone
	i=str(bin(binar))
	i=i[2:]
	inv = i[::-1]
	if i ==inv:
		return 1
	else:
		return 0
def check_pal(numb):
	i=str(numb)
	inv = i[::-1]
	if i ==inv:
		return 1
	else:
		return 0

#def summe(listy):
#	sum= 0
#	for i in range(0,len(listy)):
#		sum = 

counter=[0] # number of binary and num palindromes
	# current number being checked
for i in range(0,1000000):
	if check_pal(i) & check_bin(i):
		counter.append(i)

print (sum(counter))
#IT WORKS BIOTCH, 872187 is printed