# def main():
#     plate = input("Plate: ")
#     if is_valid(plate):
#         print("Valid")
#     else:
#         print("Invalid")


# def is_valid(s):
#     # Plate can only contain a max of 6 characters ( Numbers or Letters)
#     # Minimum of 2 characters

#     if len(s) < 2 or len(s) > 6:
#         return False

#     # Start with 2 characters
#     if s[0].isalpha() == False or s[1].isalpha() == False:
#         return False

#     # Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate;
#     # AAA22A would not be acceptable.
#     # The first number used cannot be a ‘0’.

#     i = 0
#     while 1 < len(s):
#         if s[i].isalpha() == False:
#             if s[i] == '0':
#                 return False
#             else:
#                 break
#         i += 1

#     # No periods, spaces, or punctuation marks are allowed.

#     for c in s:
#         if c in ['.', ' ', '!', '?']:
#             return False

#     # If all test pass, return True
#     return True

# main()


# def main():
#     plate = input("Plate: ")
#     if is_valid(plate):
#         print("Valid")
#     else:
#         print("Invalid")


# def is_valid(s):
#     # Plate can only contain a max of 6 characters ( Numbers or Letters)
#     # Minimum of 2 characters

#     if len(s) < 2 or len(s) > 6:
#         return False

#     # Start with 2 characters
#     if not s[0].isalpha() or not s[1].isalpha():
#         return False

#     # Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate;
#     # AAA22A would not be acceptable.
#     # The first number used cannot be a ‘0’.

#     i = 2  # Start checking from the 3rd character
#     while i < len(s):
#         if not s[i].isalpha():
#             if s[i] == '0' and i == 2:
#                 return False
#             elif not s[i].isdigit():
#                 return False
#         i += 1

#     # No periods, spaces, or punctuation marks are allowed.

#     for c in s:
#         if c in ['.', ' ', '!', '?']:
#             return False

#     # If all tests pass, return True
#     return True


# main()

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Plate can only contain a max of 6 characters (Numbers or Letters)
    # Minimum of 2 characters

    if len(s) < 2 or len(s) > 6:
        return False

    # Start with 2 characters
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable vanity plate;
    # AAA22A would not be acceptable.
    # The first number used cannot be a ‘0’.

    i = 2  # Start checking from the 3rd character
    while i < len(s):
        if not s[i].isalpha():
            if s[i] == '0' and i == 2:
                return False
            elif not s[i].isdigit():
                return False
        i += 1

    # No periods, spaces, or punctuation marks are allowed.

    for c in s:
        if c in ['.', ' ', '!', '?']:
            return False

    # If all tests pass, return True
    return True


main()
