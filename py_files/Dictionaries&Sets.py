# d = dict()
# print(type(d))

#######################################
# 1
#######################################
# Need a function that splits text into Keys
# Need a function that counts entries
# Need a function that puts entries as values
"""def sentence_analyser(text):
    sentence = {}
    for i in text:
        if i in sentence:
            sentence[i] += 1
        else:
            sentence[i] = 1
    for i, j in sentence.items():
        print("Keys: {}\t Values: {}".format(i, j))


print(sentence_analyser("Interpret this jackass"))"""


#######################################
# 2
#######################################
# function takes two dictionaries and returns one with non-duplicate keys

"""def dictionary_masher(dict1, dict2):
    dict3 = dict1.copy()
    dict3.update(dict2)
    return dict3


dictionary1 = {"name": 'Alex'}
dictionary2 = {'age': 25}


print(dictionary_masher(dictionary1, dictionary2))"""

#######################################
# 3
#######################################
"""list1 = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,]


def set_maker(list):
    returned_set = set(list)
    return returned_set


print(set_maker(list1))"""

#######################################
# 4
#######################################

"""list1 = [1,2,3,4]
list2 = [3,4,5,6]

list3 = list1 + list2
# print(list3)


def find_union(list_item1, list_item2):
    union = []
    list_item3 = list_item1 + list_item2
    for i in list_item3:
        if i not in union:
            union.append(i)
    return union


print(find_union(list1, list2))"""
