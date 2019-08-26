#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
nums = sum(range(0,101))
square_o_sums = 0
sum_o_squares = nums*nums

for i in range(0,101):
	square_o_sums += i*i
int(sum_o_squares)
int(square_o_sums)
print(sum_o_squares)
print(square_o_sums)
print(sum_o_squares-square_o_sums)
