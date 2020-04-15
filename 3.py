# Project Euler 100 - Problem 3
# https://projecteuler.net/problem=3

number = 600851475143
factor = 2
prime_factors = []

while number > 1:
    for i in range(2, factor):
        if factor % i == 0:
            #print(str(factor) + ' is not prime.')
            break
    else:
        #print(str(factor) + ' is prime.')
        if number % factor == 0:
            number = int(number / factor)
            prime_factors.append(factor)
            #print(str(factor) + ' is prime factor. New number is ' + str(number))
    factor += 1
print('The largest prime factor of the number 600851475143 is: ' + str(max(prime_factors)))