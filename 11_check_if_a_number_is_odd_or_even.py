# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.

num = int(input("enter a number: "))
if (num % 2) == 0:
   print(f"{num} is even")
else:
   print("{0} is odd".format(num))
