# Python Program to find the area of triangle
a = 6
b = 11
c = 16

# Uncomment below to take inputs from the user
# a = float(input('Enter first side: '))
# b = float(input('Enter second side: '))
# c = float(input('Enter third side: '))

# Calculate the semi-perimeter
s = (a + b + c) / 2

# Calculate the area
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

print(f'The area of the triangle is {area}')
