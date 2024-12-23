def mult(item_list):
    return item_list[0] * item_list[1]


corrupted_string = ""

with open("puzzle 3 input.txt", "r") as f:
    for line in f:
        corrupted_string += line
    f.close()
total = 0
mult_count = 0
do_list = corrupted_string.split("do()")
for each_do in do_list:
    dont_list = each_do.split("don't()")
    corrupted_list = dont_list[0].split("mul(")
    print(len(corrupted_list))
    my_ver = []
    for string in corrupted_list:
        valid_string = ""
        current_letter = ""
        current_index = 0
        while current_index < len(string):
            current_letter = string[current_index]
            valid_string += current_letter
            if current_letter == ")":
                break
            current_index += 1
        if " " in valid_string:
            continue
        if len(valid_string) < 1:
            continue
        if valid_string[-1] != ")":
            continue

        items = valid_string[0:-1].split(",")
        if len(items) != 2 or len(items[0]) > 3 or len(items[1]) > 3:
            continue
        else:
            try:
                items = [int(i) for i in items]
                total += mult(items)
                mult_count += 1
                my_ver.append(items)
                # print(valid_string, items, mult(items))
                # input()
            except:
                continue
print(total)
