#grid = []

#Griddle = [i.split() for i in grid]			#using code from http://code.jasonbhill.com/python/project-euler-problem-11/ to prepare data
#Griddle = [[int(j) for j in i] for i in Griddle]
num =[]
print("gimme dat data")
for i in range(100):
	num.append(input() + ' ')
big_girl =0
for j in range(100):
	big_girl+=int(num[j])
ten_dig = str(big_girl)
print(ten_dig)
