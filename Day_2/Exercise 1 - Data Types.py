"""
Instructions:

Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

Warning. Do not change the code on lines 1-3. Your program should work for different inputs. e.g. any two-digit number.

Example Input
39

Example Output
3 + 9 = 12
12
"""

number = input('Write a number of two digits: ')

suma = int(number[0]) + int(number[1])

print(f'{suma}')