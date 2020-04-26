# Project Euler 100 - Problem 6
# https://projecteuler.net/problem=6

# sum of squares
sum_of_squares = int()
for num in range(1, 101):
    square = num ** 2
    sum_of_squares += square

# square of sums
sum_of_nums = int()
square_of_sums = int()
for num in range(1, 101):
    sum_of_nums += num
    square_of_sums = sum_of_nums ** 2

result = square_of_sums - sum_of_squares
print('The difference between the sum of the squares of the first one hundred natural numbers '
      'and the square of the sum ' + str(result))