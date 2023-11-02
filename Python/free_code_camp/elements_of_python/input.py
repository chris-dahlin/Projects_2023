# def addtwo(a, b):
#     added = a + b
#     return added


# x = addtwo(5, 3)
# print(x)

def die(error_message):
    print(f"[ERROR] {error_message}")
    quit()


def addtwo(a, b):
    added = a + b
    return added


def split_str_to_ints(string):
    str_arr = string.split(",")

    array_of_ints = []
    for x in str_arr:
        array_of_ints.append(int(x))

    return array_of_ints


# Get the input from the user
string_of_ints = input("Enter two numbers: ")

# Split the input into a list of ints
array = split_str_to_ints(string_of_ints)

# Validate that the user has given us exactly 2
if len(array) != 2:
    die("Please enter two numbers seperated by a comma!")

# Calculate the two ints that we got from the string
result = addtwo(array[0], array[1])

print(result)
