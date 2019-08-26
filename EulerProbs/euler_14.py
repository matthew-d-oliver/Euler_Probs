#Longest collatz sequence
import time

def collatz(check_me):
	int(check_me)
	count = 1
	while check_me!=1:

		if (check_me%2)==0:	check_me/=2
		else: check_me=(check_me*3)+1
		count +=1
	return count
	
time_start = time.time()
max_checks = 0
collatz_num = 0
for i in range(13,1000000):
	j=collatz(i)
	if j>max_checks:
		collatz_num = i
		max_checks =j
elapsed_time = time.time() - time_start

print ("biggest collatz num:"+ str(collatz_num) +"   length:" +str(max_checks) +"  time taken:"+ str(elapsed_time))


