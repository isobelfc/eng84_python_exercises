# create a story using a dictionary

# define a dictionary
story1 = {
    "start": "Once upon a type there was a brave little fox cub",
    "middle": "One day while trotting through the forest he met a magpie who tried to sell him some dubious meat",
    "end": "He scared the magpie off with a growl and returned safely home"
}

# print entire dictionary
print(story1)

# print the type of the dictionary
print(type(story1))

# print only the keys
print(story1.keys())

# print only the values
print(story1.values())

# print the values individually
print(story1["start"])  # print start
print(story1["middle"])  # print middle
print(story1["end"])  # print end

# add a new key:value pair
story1["hero"] = "a brave little fox"

# check hero has added
print(story1)
