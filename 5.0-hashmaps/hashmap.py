
data = "Hello word"
my_map = {}

for item in data:
    if item not in my_map:
        my_map[item] = 1
    else:
        my_map[item] += 1

print(my_map)