value_dictionary = {}
left_list = []
right_list = []

with open("puzzle1 input.txt", "r") as f:
    for line in f:
        value_pair = [int(i) for i in line.split()]
        value_dictionary[value_pair[0]] = 0
        left_list.append(value_pair[0])
        right_list.append(value_pair[1])
    f.close()

for item in right_list:
    try:
        value_dictionary[item] += 1
    except KeyError:
        print(item, "doesn't exist")

similarity_score = 0
for key, value in value_dictionary.items():
    similarity_score += key * value

print(similarity_score)