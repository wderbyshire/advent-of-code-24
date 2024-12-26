before_order_list = {}
after_order_list = {}
updates_list = []

with open("puzzle 5 input.txt", "r") as f:
    first_half_tracker = True
    for line in f:
        if line == "\n":
            first_half_tracker = False
            continue

        if first_half_tracker:
            rule = [int(i) for i in line.strip().split("|")]

            if rule[1] in before_order_list:
                before_order_list[rule[1]].append(rule[0])
            else:
                before_order_list[rule[1]] = [rule[0]]

            if rule[0] in after_order_list:
                after_order_list[rule[0]].append(rule[1])
            else:
                after_order_list[rule[0]] = [rule[1]]
        else:
            updates_list.append([int(i) for i in line.strip().split(",")])

    f.close()

print("before rule:", before_order_list)
print("after rule:", after_order_list)

total = 0
for update in updates_list:
    safe = True
    for i in range(len(update)-1):
        if update[i+1] in after_order_list and update[i] in after_order_list[update[i+1]]:
            # print(update)
            # print(update[i], "infringes after rule of", update[i+1], after_order_list[update[i+1]])
            safe = False
            break
        elif update[i] in before_order_list and update[i+1] in before_order_list[update[i]]:
            # print(update)
            # print(update[i+1], "infringes before rule of ", update[i], before_order_list[update[i]])
            safe = False
            break
    # input()

    if safe:
        mid_index = len(update)//2
        total += update[mid_index]

# print(updates_list)
print(total)
