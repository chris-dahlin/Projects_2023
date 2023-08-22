import time

# Ask user for their name
name = input("What's your name? ")

# Remove white space from name and captitalize
name = name.strip().title()

# Say hello to the user
print(f"Hello, {name}")

time.sleep(1)

x = int(input("What's X? "))

y = int(input("What's Y? "))

print(x + y)
