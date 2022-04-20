############################################################
# 1
############################################################

wild = ['Lion', 'Zebra', 'Panther', 'Antelope']

wild.append('Elephant')

wild_2 = ['Cat', 'Dog', 'Snake', 'Dolphin']

wild.extend(wild_2)

print(wild)

wild.insert(2, 'Cheetah')
wild.pop(1)
wild.insert(1, 'Giraffe')

print()
for animal in wild:
    print(animal)

wild.sort(reverse=True)

print()
print(wild)

############################################################
# 2
############################################################

print()
pets = ('cat', 'cat', 'cat', 'dog', 'horse')

c = pets.count('cat')
print(c)

d = len(pets)

if pets.count('cat') >= (len(pets) / 2):
    print("There are too many cats on the terminal")
else:
    print("Everything is good")
