# var = 0  # Assigning 0 to var
# print(var == 0)

# var = 1  # Assigning 1 to var
# print(var == 0)

# var = 0  # Assigning 0 to var
# print(var != 0)

# var = 1  # Assigning 1 to var
# print(var != 0)

# n = int(input("Enter a number: "))
# print(n >= 100)

# if true_or_false_condition:
#     perform_if_condition_true
# else:
#     perform_if_condition_false

# Read two numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))

# # Choose the larger number
# if number1 > number2:
#     larger_number = number1
# else:
#     larger_number = number2

# # Print the result
# print("The larger number is:", larger_number)

# # Read two numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))

# # Choose the larger number
# if number1 > number2: larger_number = number1
# else: larger_number = number2

# # Print the result
# print("The larger number is:", larger_number)

# # Read three numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))

# # We temporarily assume that the first number
# # is the largest one.
# # We will verify this soon.
# largest_number = number1

# # We check if the second number is larger than current largest_number
# # and update largest_number if needed.
# if number2 > largest_number:
#     largest_number = number2

# # We check if the third number is larger than current largest_number
# # and update largest_number if needed.
# if number3 > largest_number:
#     largest_number = number3

# # Print the result
# print("The largest number is:", largest_number)

# largest_number = -999999999
# number = int(input())
# if number == -1:
#     print(largest_number)
#     exit()
# if number > largest_number:
#     largest_number = number
# # Go to line 02
# Read three numbers.


number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Check which one of the numbers is the greatest
# and pass it to the largest_number variable.

largest_number = max(number1, number2, number3)

# Print the result.
print("The largest number is:", largest_number)

