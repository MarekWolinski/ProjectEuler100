# Project Euler 100 - Problem 4
# https://projecteuler.net/problem=4

num1 = 999
num2 = 999
result = 0
for i in range(num1, 99, -1):
    for j in range(num2, 99, -1):
        multiplication = str(i * j)
        reverse = str()
        for k in range(len(multiplication)-1, -1, -1):
            reverse = reverse + multiplication[k]
        if multiplication == reverse:
            if int(reverse) > result:
                result = int(reverse)
print('The largest palindrome made from the product of two 3-digit numbers is ' + str(result))

