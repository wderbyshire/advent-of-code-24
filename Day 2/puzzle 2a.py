safe_reports = 0

with open("puzzle2 input test.txt", "r") as f:
    for line in f:
        report = [int(i) for i in line.split()]

        initial_change = report[0] - report[1]
        direction = initial_change // abs(initial_change)

        if 1 <= initial_change*direction <= 3:
            safe = 1
            for i in range(1, len(report)-1):
                change = report[i] - report[i+1]
                current_direction = change // abs(initial_change)

                if change*current_direction == 0 or change*current_direction > 3:
                    safe = 0
                    break

            safe_reports += safe
    f.close()

print(safe_reports)