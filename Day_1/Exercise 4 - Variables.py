"""
Instructions
Write a program that switches the values stored in the variables a and b.

Warning. Do not change the code on lines 1-4 and 12-18. Your program should work for different inputs. e.g. any value of a and b.

Example Input
a: 3
b: 5

Example Output
a: 5
b: 3
"""

#V1 with auxiliar variable
# number_1 = input('Write a number a: ')
# number_2 = input('Write a number b: ')
#
# aux = number_1
# number_1 = number_2
# number_2 = aux
#
# print(f'a: {number_1}')
# print(f'b: {number_2}')

#v2 without auxiliar variable
number_1 = int(input('Write a number a: '))
number_2 = int(input('Write a number b: '))


number_1 = number_1 + number_2 #se suman los valores de las dos variables y se almacena en la primera variable
number_2 = number_1 - number_2 #aqui se remmplaza haciendo las restas
number_1 = number_1 - number_2

print(f'a: {number_1}')
print(f'b: {number_2}')