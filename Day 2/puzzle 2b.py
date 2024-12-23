safe_reports = 0


def determine_safety(report_list):
    differences = [report_list[i] - report_list[i + 1] for i in range(len(report_list) - 1)]
    directions = []
    pos_dir_count = 0
    neg_dir_count = 0

    for i in differences:
        if i != 0:
            direction = i // abs(i)
        else:
            direction = 0
        directions.append(direction)
        if direction == 1:
            pos_dir_count += 1
        elif direction == -1:
            neg_dir_count += 1

    if pos_dir_count > neg_dir_count:
        bad_dir = -1
    elif pos_dir_count < neg_dir_count:
        bad_dir = 1
    else:
        return False

    for i in range(len(differences)):
        if abs(differences[i]) < 1 or abs(differences[i]) > 3:
            return False

        if directions[i] == bad_dir:
            return False

    return True


with open("puzzle2 input.txt", "r") as f:
    for line in f:
        report = [int(i) for i in line.split()]
        original_report = report.copy()
        removed = False
        valid = determine_safety(report)

        remove_index = 0
        while not valid and remove_index < len(report):
            new_report = report.copy()
            new_report.pop(remove_index)
            valid = determine_safety(new_report)
            remove_index += 1

        if valid:
            safe_reports += 1
            print(original_report, "is safe")
        else:
            print(original_report, "if unsafe")
print(safe_reports)




# def determine_safety(index1, index2, initial_direction: int | None):
#     initial_change = index1 - index2
#     abs_change = abs(initial_change)
#     # print(index1, index2, initial_change, initial_direction)
#     # input()
#
#     if abs_change < 1 or abs_change > 3:
#         return False
#     else:
#         if initial_direction is None:
#             return True
#         else:
#             direction = initial_change // abs(initial_change)
#             if direction == initial_direction:
#                 return True
#             else:
#                 return False
#
#
# safe_reports = 0
#
# with open("puzzle2 puzzle 3 input.txt", "r") as f:
#     for line in f:
#         removal_counter = False
#         report = [int(i) for i in line.split()]
#         print(report, end=" ")
#         safe = 1
#         initial_direction = None
#         removed_value = ""
#
#         report_index = 0
#         while report_index < len(report) - 1:
#             safety_result = determine_safety(report[report_index], report[report_index+1], initial_direction)
#             if not safety_result and not removal_counter and report_index == len(report) - 2:
#                 removed_value = str(report[report_index+1]) + " at index {}".format(report_index+1)
#                 report.pop(report_index+1)
#                 break
#             elif not safety_result and not removal_counter:
#                 # print("unsafe, removing index {} with value {}".format(report_index, report[report_index]))
#                 removed_value = str(report[report_index]) + " at index {}".format(report_index)
#                 report.pop(report_index)
#                 removal_counter = True
#                 report_index -= 1
#             elif not safety_result and removal_counter:
#                 # print("One already removed, unsafe")
#                 safe = 0
#                 break
#             elif safety_result and initial_direction is None:
#                 change = report[report_index] - report[report_index+1]
#                 initial_direction = change // abs(change)
#                 report_index += 1
#             else:
#                 report_index += 1
#         safe_reports += safe
#         if safe == 1:
#             print("is safe", end=" ")
#         else:
#             print("is unsafe", end=" ")
#
#         if removed_value != "":
#             print("when {} is removed".format(removed_value))
#         else:
#             print("")
# print(safe_reports)
