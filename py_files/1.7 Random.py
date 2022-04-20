import random
# 1
"""print(random.randint(1, 100))"""

# 2
"""fruit_list = ["apple", "orange", "banana", "grape", "pear"]
print(random.choice(fruit_list))"""

# 3
"""coin = ["heads", "tails"]
choice = input("Please select either heads or tails: ").lower()
result = random.choice(coin)
if result == choice:
    print("You win!!!!")
else:
    print("Bad Luck :( ")
print("The computer selected {}".format(result))"""

# 4
"""random_selection = random.randint(1, 5)
number = int(input("Please select a number between 1 and 5: "))
if number == random_selection:
    print("Well done!!!!!!")
elif number > random_selection:
    second_guess = int(input("Your guess was too high! Please try again: "))
    if second_guess != random_selection:
        print("You lose :( ")
    else:
        print("Correct!!!!")
elif number < random_selection:
    second_guess = int(input("Your guess was too low! Please try again: "))
    if second_guess != random_selection:
        print("You lose :( ")
    else:
        print("Correct!!!!!")"""

# 5
"""random_pick = random.randint(1, 10)
guess = int(input("Please enter a number between 1 and 10: "))
while guess != random_pick:
    next_guess = int(input("Please guess again: "))
    if next_guess == random_pick:
        break
print("You have guessed the right number! {}".format(random_pick))"""

# 6
"""random_pick = random.randint(1, 10)
guess = int(input("Please enter a number between 1 and 10: "))
while guess != random_pick:
    if guess > random_pick:
        guess = int(input("You were too high! Guess again: "))
    elif guess < random_pick:
        guess = int(input("You were too low! Guess again: "))
    else:
        break
print("You have guessed the right number! {}".format(random_pick))"""

# 7
"""student_score = 0
number1, number2 = [random.randint(1, 100), random.randint(1, 100)]
question1 = int(input("What is the result of {} + {}?: ".format(number1, number2)))
print("Answer: {}".format(number1 + number2))
if question1 == number1 + number2:
    student_score += 1

number3, number4 = [random.randint(1, 100), random.randint(1, 100)]
question2 = int(input("What is the result of {} - {}?: ".format(number3, number4)))
print("Answer: {}".format(number3 - number4))
if question2 == number4 - number3:
    student_score += 1

number5, number6 = [random.randint(1, 100), random.randint(1, 100)]
question3 = float(input("What is the result of {} / {}?: ".format(number5, number6)))
print("Answer: {}".format(number5 / number6))
if question3 == number5 / number6:
    student_score += 1

number7, number8 = [random.randint(1, 100), random.randint(1, 100)]
question4 = int(input("What is the result of {} * {}?: ".format(number7, number8)))
print("Answer: {}".format(number7 * number8))
if question4 == number7 * number8:
    student_score += 1

number9, number10 = [random.randint(1, 100), random.randint(1,100)]
question5 = int(input("What is the result of {} ** {}?: ".format(number9, number10)))
print("Answer: {}".format(number9 ** number10))
if question5 == number9 ** number10:
    student_score += 1

print("You got {} / 5 on the test".format(student_score))"""

# 8
"""blue_hint = "You are probably feeling blue right now"
red_hint = "You are probably red with rage right now"
yellow_hint = "You are probably feeling yellow and ill"
green_hint = "You are probably green with envy right now"
orange_hint = "You are probably blushing orange right now"

color_list = ["blue", "red", "orange", "yellow", "green"]
random_color = random.choice(color_list)
print(color_list)

color_choice = input("Please select a color from the list: ").lower()
while color_choice in color_list:
    if color_choice == random_color:
        break
    elif random_color == "blue":
        print(blue_hint)
        color_choice = input("Please select a color from the list: ").lower()

    elif color_choice == random_color:
        break

    elif random_color == "red":
        print(red_hint)
        color_choice = input("Please select a color from the list: ").lower()

    elif color_choice == random_color:
        break

    elif random_color == "orange":
        print(orange_hint)
        color_choice = input("Please select a color from the list: ").lower()

    elif color_choice == random_color:
        break

    elif random_color == "yellow":
        print(yellow_hint)
        color_choice = input("Please select a color from the list: ").lower()
    elif color_choice == random_color:
        break

    elif random_color == "green":
        print(green_hint)
        color_choice = input("Please select a color from the list: ").lower()
print("Correct, it is in the list!")"""





