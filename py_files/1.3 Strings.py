# 1
"""name = input("Please enter your name: ")
name_length = len(name)
print(name_length)"""

# 2
"""first_name = input("Please enter your first name: ")
surname = input("Please enter your surname: ")
full_name = first_name + " " + surname
print(full_name, ":", len(full_name))"""

# 3
"""first_name = str.lower(input("Please enter your first name: "))
surname = str.lower(input("Please enter your surname: "))
full_name = first_name.capitalize() + " " + surname.capitalize()
print(full_name)"""

# 4
# Baa baa black sheep, have you any wool?
"""rhyme = input("Please enter the first line of a nursery rhyme: ")
length = len(rhyme)
print("You can enter numbers between 0 and {}".format(length))
start_number = int(input("Please enter a starting number: "))
end_number = int(input("Please enter an end number: "))
print(rhyme[start_number : end_number])"""

# 5
"""word = input("Please enter a word: ")
upper_case = str.upper(word)
print(upper_case)"""

# 6
"""first_name = input("Please enter your first name: ")
if len(first_name) < 5:
    surname = input("Please enter your surname: ")
    full_name = first_name.upper() + surname.upper()
    print(full_name)
else:
    print(first_name.lower())"""

# 7
"""vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
word = input("Please enter a word: ")
new_word = word[0]
if new_word in vowels:
    pig_latin = word + "way"
    print(pig_latin)
else:
    word = word.replace(word[0], "")
    pig_latin = word + new_word + "ay"
    print(pig_latin.lower())"""
