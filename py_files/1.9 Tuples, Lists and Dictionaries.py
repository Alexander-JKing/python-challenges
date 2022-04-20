# 1
"""countries = ("Ireland", "England", "Canada", "Spain", "Scotland")
print(countries)
country = input("Please select one of the countries from the list: ")
print("You have selected {}, with an index of {} in the list!".format(country, countries.index(country)))"""

# 2
"""countries = ("Ireland", "England", "Canada", "Spain", "Scotland")
print(countries)
country = input("Please select one of the countries from the list: ")
print("You have selected {}, with an index of {} in the list!".format(country, countries.index(country)))
index = int(input("\nPlease select an index from the list: "))
print("You have selected the index {}, which is the country '{}'!".format(index, countries[index]))"""

# 3
"""sports = ["Football", "Hurling"]
favourite_sport = input("What is your favourite sport?: ")
sports.append(favourite_sport)
sports.sort()
print(sports)"""

# 4
"""subjects = ["Maths", "English", "Art", "History", "Geography", "Biology"]
print(subjects)
del_subject = input("Which of these subjects is your least favourite?: ")
subjects.remove(del_subject)
print(subjects)"""

# 5
"""food1 = input("What is one of your favourite foods?: ")
food2 = input("What is one of your favourite foods?: ")
food3 = input("What is one of your favourite foods?: ")
food4 = input("What is one of your favourite foods?: ")
foods = {1: food1, 2: food2, 3: food3, 4: food4}
print(foods)
items = foods.items()
for item in items:
    print(item)
del_food = int(input("Which number would you like to delete?: "))
del foods[del_food]
print(sorted(foods.values()))"""

# 6
"""color_list = ["red", "blue", "green", "pink", "purple", "yellow", "brown", "black", "white", "orange"]
print(len(color_list))
start_number = int(input("Please enter a start number between 0 and 4: "))
end_number = int(input("Please enter an end number between 5 and 9: "))
print(color_list[start_number:end_number])"""

# 7
"""list1 = [100, 200, 300, 400]
for number in list1:
    print(number)
user_number = int(input("Please enter a 3 digit number: "))
if user_number in list1:
    print("The number you entered is in this list, and has an index of {}".format(list1.index(user_number)))
else:
    print("That is not in the list!")"""

# 8
"""guest_list = []
guest1 = input("Please enter the name of a guest you would like to invite: ")
guest2 = input("Please enter another guest name: ")
guest3 = input("Please enter another guest name: ")
guest_list.extend((guest1, guest2, guest3))
extra_guest = True
while extra_guest is True:
    question = input("Would you like to enter another guest name?: ").lower()
    if question == "yes":
        next_guest = input("\nPlease enter the name of the guest you would like to invite: ")
        guest_list.append(next_guest)
    elif question == "no":
        extra_guest = False
print("You have invited {} guests to the party".format(len(guest_list)))"""

# 9
"""guest_list = []
guest1 = input("Please enter the name of a guest you would like to invite: ")
guest2 = input("Please enter another guest name: ")
guest3 = input("Please enter another guest name: ")
guest_list.extend((guest1, guest2, guest3))
extra_guest = True
while extra_guest is True:
    question = input("Would you like to enter another guest name?: ").lower()
    if question == "yes":
        next_guest = input("\nPlease enter the name of the guest you would like to invite: ")
        guest_list.append(next_guest)
    elif question == "no":
        extra_guest = False
print("You have invited {} guests to the party".format(len(guest_list)))

for guest in guest_list:
    print(guest)
chosen_guest = input("Please enter one of the names on the list: ")
print("The position of guest {} on the list, is {}".format(chosen_guest, guest_list.index(chosen_guest) + 1))
last_chance = input("Are you sure you wish to invite this guest to the party?: ").lower()
if last_chance == "no":
    chosen_guest_index = guest_list.index(chosen_guest)
    del guest_list[chosen_guest_index]
else:
    pass
for guest in guest_list:
    print(guest)"""

# 10
"""tv_programmes = ["Mandalorian", "Mad Men", "Mr. Robot", "Game of Thrones", "Queen's Gambit"]
for tv_programme in tv_programmes:
    print(tv_programme)
user_show = input("\nPlease enter one of your favourite tv shows: ")
user_index = int(input("Which position would you like this show to be in?: "))
tv_programmes.insert(user_index, user_show)
print()
for tv_programme in tv_programmes:
    print(tv_programme)"""

# 11
"""nums = []
condition1 = True
while condition1 is True:
    user_number = int(input("Please enter a number to add to the list: "))
    nums.append(user_number)
    if len(nums) == 3:
        question = input("Do you want the last number you entered {}, to be saved?: ".format(nums[2])).lower()
        if question == "no":
            nums.remove(nums[2])
            condition1 = False
        else:
            break
    else:
        print(nums)
print(nums)"""
