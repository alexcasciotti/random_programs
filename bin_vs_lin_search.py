import json
import random
import time

def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1
def linear_search(list, target):
    for x in list:
        if(x == target):
            return list.index(x)
    return -1

data = {}
english_dict = []

with open("/Users/macbook/Downloads/words_dictionary.json") as json_file:
    data = json.load(json_file)
    for x in data:
        english_dict.append(x)

# for x in range(len(english_dict)):
#     print(f'({x}) {english_dict[x]}')

english_dict.sort()

while True:
    try:
        upper_bound = int(input("How many words?\n"))
        if(upper_bound <= 0):
            print("Enter a value greater than zero.")
        else:
            break
    except ValueError:
        print("Enter an integer value.")

start = time.time()
for x in range(1, upper_bound):
    random_word = english_dict[random.randint(0,len(english_dict)-1)]
    print(f"({x})\nBinary searching '{random_word}'...")
    result = binary_search(english_dict, 0, len(english_dict) - 1, random_word)
    if(result != -1):
        print("Found!")
    else:
        print("Not found.")
end = time.time()
bin_search_time = round(end - start, 7)



# start = time.time()
# for x in range(1, upper_bound):
#     random_word = english_dict[random.randint(0,len(english_dict)-1)]
#     print(f"({x})\nLinear searching '{random_word}'...")
#     result = linear_search(english_dict, random_word)
#     if(result != -1):
#         print("Found!")
#     else:
#         print("Not found.")
# end = time.time()
# lin_search_time = round(end - start, 7)

print(f"\nBinary search found {upper_bound} items in {bin_search_time}s\n")
# print(f"\nLinear search found {upper_bound} items in {lin_search_time}s\n")

