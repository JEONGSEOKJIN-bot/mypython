rum_num = 5

for row in range(rum_num):

    for col in range(rum_num):
        if row % 2 == 1 and col % 2 == 1  :
            print(" ", end="")
        else:
            print("*", end="")
    print() 

for i in range(3):
    print()


for row in range(rum_num):

    for col in range(rum_num):
        if row == col:
            print(" ", end="")
        else:
            print("*", end="")
    
    print()