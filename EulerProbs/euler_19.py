'''You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?'''
weekDays = ['Mon',
			'Tue',
			'Wed',
			'Thu',
			'Fri',
			'Sat',
			'Sun']


monthNames = ['Jan',
		'Feb',
		'Mar',
		'Apr',
		'May',
		'Jun',
		'Jul',
		'Aug',
		'Sep',
		'Oct',
		'Nov',
		'Dec']


months = [[1,31],
		[2,28],
		[3,31],
		[4,30],
		[5,31],
		[6,30],
		[7,31],
		[8,31],
		[9,30],
		[10,31],
		[11,30],
		[12,31]]

def upDate(dt, k):
	if ((int(dt[3])%4)==0)&(int(dt[1])==28)&(int(dt[2])==2):
		


	elif int(dt[0])!=7:dates[k][0]=list(int(dates[k][0])+1)
	else:
		dates[k][0]='1'
	if (int(dt[2])==12)&(int(dt[1])==31):
		

		dates[k][3]=
	if int(dt[1])!=months[int(dt[2])-1][1]: dates[k][1]=list(int(dates[k][1])+1)
	else:
		dates[k][1]='1'
		dates[k][2]=list(int(dates[k][2])+1)
	if int(dt[])


sundays = 0
dates = [['1', '1', '1', '1900']]
for i in range(12):
	upDate(dates[i][], i)