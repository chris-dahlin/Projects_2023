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


# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))

# # Check which one of the numbers is the greatest
# # and pass it to the largest_number variable.

# largest_number = max(number1, number2, number3)

# # Print the result.
# print("The largest number is:", largest_number)

# flower = input("What is your favorite flower?")

# if flower == "Spathiphyllum":
#     print("Yes - Spathiphyllum is the best plant ever!")
# else:
#     print("No, I want a big Spathiphyllum!")


# name = input("Enter flower name: ")

# if name == "Spathiphyllum":
#     print("Yes - Spathiphyllum is the best plant ever!")
# elif name == "spathiphyllum":
#     print("No, I want a big Spathiphyllum!")
# else:
#     print("Spathiphyllum! Not", name + "!")


# flower = input("Enter flower name: ")

# if flower == "Spathiphyllum":
#     print("Yes - Spathiphyllum is the best plant ever!")
# elif flower == "spathiphyllum":
#     print("No, I want a big Spathiphyllum!")
# else:
#     print("Spathiphyllum! Not", flower + "!")


# income = float(input("Enter the annual income: "))

# if income <= 85528:
#         tax = 0.18 * income - 556.02
# else:
#     tax = 14839.02 + 0.32 * (income - 85528)
    
# # print("The tax is: ", max(tax, 0))  # Ensure that the tax is not negative

# tax = round(tax, 0)
# print("The tax is:", tax, "thalers")
# # # Example usage:
# # citizen_income = float(input("Enter the citizen's income in thalers: "))
# # tax_due = calculate_tax(citizen_income)
# # print(f'The tax due is: {tax_due:.2f} thalers')


# year = int(input("Enter a year: "))

# if year < 1582:
# 	print("Not within the Gregorian calendar period")
# else:
# 	if year % 4 != 0:
# 		print("Common year")
# 	elif year % 100 != 0:
# 		print("Leap year")
# 	elif year % 400 != 0:
# 		print("Common year")
# 	else:
# 		print("Leap year")


# x = int(input("input an x value:"))

# if x > 5:  # True
#     if x == 6:  # False
#         print("nested: x == 6")
#     elif x == 10:  # True
#         print("nested: x == 10")
#     else:
#         print("nested: else")
# else:
#     print("else")


# # Store the current largest number here.
# largest_number = -999999999

# # Input the first value.
# number = int(input("Enter a number or type -1 to stop: "))

# # If the number is not equal to -1, continue.
# while number != -1:
#     # Is number larger than largest_number?
#     if number > largest_number:
#         # Yes, update largest_number.
#         largest_number = number
#     # Input the next number.
#     number = int(input("Enter a number or type -1 to stop: "))

# # Print the largest number.
# print("The largest number is:", largest_number)


# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)

