safe_reports = 0

with open("puzzle2 input.txt", "r") as f:
    for line in f:
        report = [int(i) for i in line.split()]
        initial_change = report[0] - report[1]
        if initial_change == 0:
            continue

        direction = initial_change // abs(initial_change)

        if 1 <= initial_change*direction <= 3:
            safe = 1
            for i in range(1, len(report)-1):
                change = report[i] - report[i+1]
                if change == 0:
                    safe = 0
                    break

                current_direction = change // abs(change)

                if change*current_direction > 3 or direction != current_direction:
                    safe = 0
                    break

            safe_reports += safe
    f.close()

print(safe_reports)