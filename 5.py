# Project Euler 100 - Problem 5
# https://projecteuler.net/problem=5

num = 0

while True:
    num += 20
    counter = 0
    for i in range(1, 21):
        is_divisible = num % i
        if is_divisible == 0:
            counter += 1
            if counter == 20:
                print('The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is ' + str(num))
                exit()