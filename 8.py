# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product.
# What is the value of this product?
# 1000-digit number is in the file 'Problem_8_data.txt'.

def file_open(file_name):
    # opens data file

    with open(file_name) as f:
        number = f.read()
    return number


def adjacent_digit(number, lenght):
    # returns max adjacent digit of given lenght in given number

    starting_digit = 0
    ending_digit = lenght
    max_adjacent = int()
    while ending_digit <= len(number):
        temp_adjacent = 1
        for i in range(starting_digit, ending_digit):
            temp_adjacent = temp_adjacent * int(number[i])
        if temp_adjacent > max_adjacent:
            max_adjacent = temp_adjacent
        starting_digit += 1
        ending_digit += 1
    return max_adjacent


number = file_open('Problem_8_data.txt')
max_adjacent = adjacent_digit(number, 13)
print('The answer is: ', max_adjacent)
