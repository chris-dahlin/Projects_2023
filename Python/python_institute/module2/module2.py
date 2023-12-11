# print(111_111_111)

# print(0o123)

# print(0x123)

# print(True > False)
# print(True < False)

# print('"I\'m" \n ""learning"" \n """Python"""')

# print(2 * 3)
# print(2 * 3.)
# print(2. * 3)
# print(2. * 3.)


# print(6 / 3)
# print(6 / 3.)
# print(6. / 3)
# print(6. / 3.)

# print(6 // 3)
# print(6 // 3.)
# print(6. // 3)
# print(6. // 3.)

# print(6 // 4)
# print(6. // 4)

# print(6 / 4)
# print(6. / 4)

# print(-6 // 4)
# print(6. // -4)

# print(12 % 4.5)

# print(9 % 6 % 2)

# print(2 ** 2 ** 3)

# print(2 * 3 % 5)

# print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)

# print((2 ** 4), (2 * 4.), (2 * 4))

# print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))

# print((2 % -4), (2 % 4), (2 ** 3 ** 2))

# Off Limit keywords for variables
# ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# var = 1
# account_balance = 1000.0
# client_name = 'John Doe'
# print(var, account_balance, client_name)
# print(var)

# var = "3.8.5"
# print("Python version: " + var)

# var = 100
# var = 200 + 300
# print(var)

# john = 1
# mary = 2
# adam = 3

# print(john, mary, adam, sep=",")

# total_apples = john + mary + adam

# print(total_apples)

# kilometers = 12.25
# miles = 7.38

# miles_to_kilometers = miles * 1.61
# kilometers_to_miles = kilometers * .621371

# print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
# print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

# x = 0
# x = float(x)
# y = 3 * x ** 3 - 2 * x ** 2 + 3 * x - 1
# print("y =", y)
# x = 1
# x = float(x)
# y = 3 * x ** 3 - 2 * x ** 2 + 3 * x - 1
# print("y =", y)
# x = -1
# x = float(x)
# y = 3 * x ** 3 - 2 * x ** 2 + 3 * x - 1
# print("y =", y)

#this program computes the number of seconds in a given number of hours
# this program has been written two days ago

# a = 2 # number of hours
# seconds = 3600 # number of seconds in 1 hour

# print("Hours: ", a) #printing the number of hours
# # print("Seconds in Hours: ", a * seconds) # printing the number of seconds in a given number of hours
# print("Seconds in Hours: ", a * seconds)
# #here we should also print "Goodbye", but a programmer didn't have time to write any code
# print("Goodbye")
# #this is the end of the program that computes the number of seconds in 3 hours
# a = 3
# print("Seconds in Hours: ", a * seconds)


# print("Tell me anything...")
# anything = input()
# print("Hmm...", anything, "... Really?")

# anything = input("Enter a number: ")
# something = anything ** 2.0
# print(anything, "to the power of 2 is", something)

# fnam = input("May I have your first name, please? ")
# lnam = input("May I have your last name, please? ")
# print("Thank you.")
# print("\nYour name is " + fnam + " " + lnam + ".")

# print("+" + 10 * "-" + "+")
# print(("|" + " " * 10 + "|\n") * 5, end="")
# print("+" + 10 * "-" + "+")
# Output
# +----------+
# |          |
# |          |
# |          |
# |          |
# |          |
# +----------+

# leg_a = float(input("Input first leg length: "))
# leg_b = float(input("Input second leg length: "))
# print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))

# a = float(input("Please input A: "))
# # input a float value for variable a here

# b = float(input("Please input B: "))
# # input a float value for variable b here


# # output the result of addition here
# print("A + B = ", a + b)
# # output the result of subtraction here
# print("A - B = ", a - b)
# # output the result of multiplication here
# print("A * B = ", a * b)
# # output the result of division here
# print("A / B = ", a / b)

# print("\nThat's all, folks!")

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
print((hour+(mins+dura)//60)%24,":",(mins+dura)%60)