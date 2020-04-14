# Project Euler 100 - Problem 2
# https://projecteuler.net/problem=2

term1 = 1
term2 = 2
sol = 0

while term1 < 4000000 and term2 < 4000000:
    if term1 % 2 == 0:
        sol = sol + term1
    if term2 % 2 == 0:
        sol = sol + term2
    term1 = term1 + term2
    term2 = term1 + term2

print('The sum of the even-valued terms below 4.000.000 is ' + str(sol))