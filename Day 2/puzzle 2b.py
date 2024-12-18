def valid_difference(diff):
    return 1 <= abs(diff) <= 3

def valid_direction(initial_direction, current_direction):
    return initial_direction == current_direction

safe_reports = 0

with open("puzzle2 input.txt", "r") as f:
    for line in f:
        removal_counter = False
        report = [int(i) for i in line.split()]
        initial_change = report[0] - report[1]

        if initial_change == 0:
            report.pop(0)
            initial_change = report[0] - report[1]
            removal_counter = True
            if initial_change == 0:
                continue
        elif not valid_difference(initial_change):
            if removal_counter:
                continue
            else:
                report.pop(0)
                initial_change = report[0] - report[1]
                removal_counter = True
                if not valid_difference(initial_change):
                    continue
        else:
            initial_direction = initial_change // abs(initial_change)
            safe = 1
            for i in range(1, len(report) - 1):
                change = report[i] - report[i + 1]
                if change == 0 or not valid_difference(change):
                    if removal_counter:
                        safe = 0
                        break
                    else:
                        change = report[i - 1] - report[i + 1]
                        if change == 0 or not valid_difference(change):
                            safe = 0
                            break
                        else:
                            removal_counter = True

                else:
                    direction = change // abs(change)

                    if not valid_direction(initial_direction, direction):
                        if removal_counter:
                            safe = 0
                            break
                        else:
                            change = report[i - 1] - report[i + 1]
                            if change == 0 or not valid_difference(change):
                                safe = 0
                                break
                            else:
                                direction = change // abs(change)
                                if not valid_direction(initial_direction, direction):
                                    safe = 0
                                    break
                                else:
                                    removal_counter = True

            safe_reports += safe
print(safe_reports)