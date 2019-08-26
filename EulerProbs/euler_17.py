'''If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.'''
#Euler problem 17 by moliver

nums = {1:['One','Eleven'],
		2:['Two','Twelve','Twenty'],
		3:['Three','Thirteen','Thirty'],
		4:['Four','Fourteen','Forty'],
		5:['Five','Fifteen','Fifty'],
		6:['Six','Sixteen','Sixty'],
		7:['Seven','Seventeen','Seventy'],
		8:['Eight','Eighteen','Eighty'],
		9:['Nine','Nineteen','Ninety'],
		0:['','Ten','Hundred']}
def vert2lett(j):
	x=str(j)
	if len(x)==1:
		return str(nums[j][0])
	elif len(x) == 2:
		if x[0]=='1':
			return nums[int(x[1])][1]
		elif x[0]!='1':
			tenner = nums[int(x[0])][2]
			oner = nums[int(x[1])][0]
			return tenner + oner
	elif len(x) ==3:
		hundo = nums[int(x[0])][0] +'Hundred'
		if x[-2:]=='00':
			return hundo
		return hundo +'And'+ vert2lett(j-(int(x[0])*100))



counter = 0	
ranger = 999	
for i in range (1,ranger+1):
	counter+=len(vert2lett(i))

print(counter+11)
print(len(vert2lett(342)))
print(len(vert2lett(115)))