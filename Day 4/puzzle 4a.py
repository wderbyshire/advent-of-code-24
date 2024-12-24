def count_xmas(items: list[str], diagonal: bool):
    diagonal_items = []

    total = 0
    for row_index, row in enumerate(items):
        current_count = row.count("XMAS")
        current_count += row.count("SAMX")
        total += current_count
        if diagonal:
            string_list = list(row)
            string_list = [""]*row_index + string_list
            for letter_index, letter in enumerate(string_list):
                if letter != "":
                    if len(diagonal_items)-1 < letter_index:
                        diagonal_items.append(letter)
                    else:
                        diagonal_items[letter_index] += letter
        print(row, current_count)
    print(total)
    print()

    if diagonal:
        diagonal_count = count_xmas(diagonal_items, False)
        return total + diagonal_count
    else:
        return total


pinput = []
v_pinput = []

with open("puzzle 4 input.txt", "r") as f:
    for line in f:
        pstring = line.strip()
        pinput.append(pstring)

        if len(v_pinput) == 0:
            for letter in pstring:
                v_pinput.append(letter)
        else:
            for index, letter in enumerate(pstring):
                v_pinput[index] = letter + v_pinput[index]

xmas_count = count_xmas(pinput, True) + count_xmas(v_pinput, True)
print(xmas_count)