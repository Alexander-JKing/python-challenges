# 1
"""total = 0
while total < 50:
    number = int(input("Please enter a number: "))
    total += number
    print("The total is {}".format(total))"""

# 2
"""request = 0
while request < 5:
    request = int(input("Please enter a number: "))
    print("The last number you entered was {}".format(request))
    if request >= 5:
        print("[You have exceeded your selection]")"""

# 3
"""number1 = int(input("Please enter a number: "))
number2 = int(input("Please enter a second number: "))
total = number1 + number2
request = input("Do you wish to add another number: ")
answer_list = ["Yes", "Y", "YES", "yes", "y"]
while request in answer_list:
    next_number = int(input("Please add another number: "))
    total += next_number
    request = input("Do you wish to add another number: ")
print("The total amounts to {}, after termination".format(total))"""

# 4
"""count = 0
answer_list = ["Yes", "Y", "YES", "yes", "y"]
name = input("Please enter guest name: ")
count += 1
print("\n{} has been invited ({} invites so far)".format(name, count))
request = input("Do you wish to add another guest to the list?: ")
while request in answer_list:
    name = input("Please enter guest name: ")
    count = count + 1
    print("\n{} has been invited ({} invites so far)".format(name, count))
    request = input("\nDo you wish to add another guest to the list?: ")
print("\n{} guests invited to the 'party'".format(count))"""

# 5
"""attempts = 0
compnum = 50
print("Guess which number is the 'compnum' value!!")
guess = int(input("Please enter a number: "))
while guess != compnum:
    if guess > compnum:
        print("Your guess is too high, try a little lower!")
        attempts += 1
        guess = int(input("\nPlease enter another number: "))
    elif guess < compnum:
        print("Your guess is too low, try a little higher!")
        attempts += 1
        guess = int(input("\nPlease enter another number: "))
print("Well done, you got it!\nIt took you {} attempt!".format(attempts + 1))"""

# 6
"""number = int(input("Please enter a number: "))
while number < 10 or number > 20:
    if number < 10:
        print("Too low, please try again! ")
        number = int(input("Please enter a number: "))
    elif number > 20:
        print("Too high, please try again! ")
        number = int(input("Please enter a number: "))
print("Thank you!, Your number was {}".format(number))"""

# 7
"""bottle_number = 10
while bottle_number > 0:
    print("There are {} green bottles hanging on the wall,".format(bottle_number))
    print("{} green bottles hanging on the wall,".format(bottle_number))
    print("and if 1 green bottle should accidentally fall.....")
    bottle_number -= 1
    answer = int(input("\nHow many green bottles will be hanging on the wall?: "))
    if answer == bottle_number:
        print("There are {} green bottles hanging on the wall".format(bottle_number))
    else:
        print("No, try again")
        answer = int(input("How many green bottles will be hanging on the wall?: "))
print("\nThere are no more green bottles hanging on the wall!")"""




