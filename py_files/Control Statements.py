###################################
# 1
###################################
"""release_year = '1991'
answer = input("When was python first released?: ")

if answer == release_year:
    print("Congratulations! That is correct")
else:
    print("No, incorrect year")"""

###################################
# 2
###################################
"""password = 'random'
correct = False

while correct is False:
    enter_password = input("Pleas enter the password: ")
    if enter_password == password:
        print("Access Granted")
        correct = True
    else:
        print("Incorrect, please try again:")"""

###################################
# 3
###################################

"""record = 1
sum = 0
for i in range(2, 101, 2):
    print("Even Number {}: {}".format(record, i))
    record += 1
    sum += i
print("\nFinished with sum of: ", sum)"""

###################################
# 4
###################################
"""even_count = 1
odd_count = 1
even_sum = 0
odd_sum = 0

for even in range(0, 13, 2):
    print("Even Number {}: {}".format(even_count, even))
    even_sum += 1
    even_count += 1
    for odd in range(1, 13, 2):
        print("Odd Number {}: {}".format(odd_count, odd))
        odd_sum += 1
        odd_count += 1
    print("\nCompleted Run")"""

###################################
# 5
###################################

divisible = 0
for i in range(0, 201):
    if i % 3 != divisible:
        continue
    elif i == 0:
        continue
    elif type(i) != int:
        continue
    print("Value: ", i)



