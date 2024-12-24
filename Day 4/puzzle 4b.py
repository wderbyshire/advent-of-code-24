pinput = []

with open("puzzle 4 input.txt", "r") as f:
    for line in f:
        pinput.append(list(line.strip()))

xmas_count = 0
for row in range(1, len(pinput)-1):
    for col in range(1, len(pinput[row])-1):
        if pinput[row][col].upper() == "A":
            lr_diag = pinput[row-1][col-1] + "A" + pinput[row+1][col+1]
            rl_diag = pinput[row+1][col-1] + "A" + pinput[row-1][col+1]

            if (lr_diag.upper() == "SAM" or lr_diag.upper() == "MAS") and (rl_diag.upper() == "SAM" or rl_diag.upper() == "MAS"):
                xmas_count += 1
                pinput[row][col] = pinput[row][col].lower()
                pinput[row - 1][col - 1] = pinput[row-1][col-1].lower()
                pinput[row + 1][col + 1] = pinput[row+1][col+1].lower()
                pinput[row + 1][col - 1] = pinput[row+1][col-1].lower()
                pinput[row - 1][col + 1] = pinput[row-1][col+1].lower()

print(xmas_count)
for i in pinput:
    print("".join(i))



