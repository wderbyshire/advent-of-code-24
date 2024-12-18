def insert_in_order(item, list_to_insert: list[int]):
    pos = len(list_to_insert)
    while pos > 0 and list_to_insert[pos-1] > item:
        pos -= 1

    list_to_insert.insert(pos, item)

    return list_to_insert

left_list = []
right_list = []

with open("puzzle1 input.txt", "r") as f:
    for line in f:
        value_pair = [int(i) for i in line.split()]
        left_list = insert_in_order(value_pair[0], left_list)
        right_list = insert_in_order(value_pair[1], right_list)
    f.close()

total = 0
for i in range(len(left_list)):
    current_diff = abs(left_list[i] - right_list[i])
    total += current_diff

print(total)