row_num = 5

for row in range(row_num):

    for value in range(row_num - row - 1):
        print(" ", end="")

    for col in range(2*row + 1):
        if col == 0 or col == 2*row or row_num == row + 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()