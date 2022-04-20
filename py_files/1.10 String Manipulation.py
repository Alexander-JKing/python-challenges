# 1
"""first_name = input("Please enter your first name: ")
print(len(first_name))
last_name = input("Please enter your last name: ")
print(len(last_name))
full_name = first_name + " " + last_name
print(full_name)
print(len(first_name + last_name))"""

# 2
"""favourite_subject = input("Please enter your favourite subject: ")
for letter in favourite_subject:
    print(letter, end="-")"""

# 3
"""poem = "One equal temper of heroic hearts, Made weak by time and fate,\nbut strong in will, To strive, to seek, to find,\nand not to yield."
print(poem)
start_point = int(input("Please enter a start point for the poem: "))
end_point = int(input("Please enter an end point for the poem: "))
print(poem[start_point:end_point])"""

# 4
"""condition1 = True
while condition1 is True:
    uppercase = input("Please type in a word in upper case: ")
    if uppercase.islower():
        print("\nIn UPPER case please!")
    else:
        print(uppercase)
        condition1 = False"""

# 5
"""eircode = input("Please enter your eircode: ")
three_letters = eircode[0:3].upper()
print(three_letters)"""

# 6
"""vowels = ["a", "e", "i", "o", "u"]
count_of_vowels = 0
user_name = input("Please enter your name: ").lower()
for letter in user_name:
    if letter in vowels:
        count_of_vowels += 1
print(count_of_vowels)"""

# 7
"""new_password = input("Please enter a new password: ")
verification = input("Please enter password again: ")
if new_password == verification:
    print("Thank you!")
elif new_password == new_password.lower() and verification == verification.upper():
    print("The passwords must be in the same case!")
elif new_password == new_password.upper() and verification == verification.lower():
    print("The passwords must be in the same case!")
elif new_password == new_password.title() and verification == verification:
    print("The passwords must be in the same case!")
elif new_password == new_password and verification == verification.title():
    print("The passwords must be in the same case!")
else:
    print("Incorrect!")"""

# 8


"""def reverse_slice(text):
    return text[::-1]


user_word = reverse_slice(input("Please enter a word: "))
for letter in user_word:
    print(letter)"""

