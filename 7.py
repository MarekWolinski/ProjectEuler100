# Project Euler 100 - Problem 6
# https://projecteuler.net/problem=6

prime_counter = 2
number = 3

while prime_counter <= 10001:
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        if prime_counter == 10001:
            print('The 10 001st prime number is ' + str(number))
        prime_counter += 1
    number += 1