# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath

a = 10
b = 16
c = 20

# calculate the discriminant
d = (b ** 2) - (4 * a * c)

# find two solutions
sol1 = (-b - cmath.sqrt(d)) / (2 * a)
sol2 = (-b + cmath.sqrt(d)) / (2 * a)

print(f'The solution are {sol1} and {sol2}')
