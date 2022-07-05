rum_num = 5

for row in range(rum_num):

    for col in range(rum_num):
        if row == 0 or row == col or row == rum_num - 1 or rum_num == row + col +1:
            print("*", end="")
        else:
            print(" ", end="")
    
    print()