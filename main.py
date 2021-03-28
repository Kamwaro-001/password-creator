# password Creator
import time
import re

print("Hello, I am going to take you through creating a Password.\n")
time.sleep(1)
print("Rules: ")
rules = ["password length must be 6 or longer", "password must have special characters",
         "password must contain a number", "password must contain at least one uppercase letter"]
for each in rules:
    print(each)
    time.sleep(1.0)

global store_int
global store_uppercase


# this function converts a string into a list of characters
# then converts any number in the list to integer type
# it then returns the final list
def convert(string):
    list1 = []
    list1[:0] = string
    global store_int
    store_int = []
    store_str = []
    global store_uppercase
    store_uppercase = []

    for n in list1:
        if n.isdigit():
            store_int.append(int(n))
        elif n.isupper():
            store_uppercase.append(n)
        else:
            store_str.append(n)

    stored = store_int + store_uppercase + store_str

    return stored


def create_pass():
    pass1 = input("Enter a password: ")
    convert(pass1)

    if len(pass1) < 6:
        print("Password is too short")
        create_pass()

    special_characters = re.compile('[@_!#$%^&*()<>?/|}{~:,.]')

    if (special_characters.search(pass1) is None) or not store_int or not store_uppercase:
        print("Your password must contain a number, an uppercase letter and a special character!")
        create_pass()

    pass2 = input("Please confirm the password: ")

    if pass1 != pass2:
        print("The passwords do not match!")
        create_pass()
    else:
        print("Your password has been created successfully!")
        time.sleep(1)
        print("\nThe password You Have Created is -> " + pass1)
        exit()


create_pass()