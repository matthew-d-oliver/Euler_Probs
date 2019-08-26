'''2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?'''
#Euler problem 16
val = 2**1000
val_digits = str(val)
counter = 0
for i in range(0,len(val_digits)):
	counter += int(val_digits[i])
print(str(counter)