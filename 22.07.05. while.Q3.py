rum_num = 5

row = 0
while row < rum_num:
    row = row + 1
    
    col = 0
    while col < rum_num:
        col = col + 1
        if row % 2 == 0 and col % 2 == 0:
            print(" ", end="")
        else:
            print("*", end="")
    print()
    
v = 0
while v < 2:
    print()
    v = v + 1
        
row = 0
while row < rum_num:
    row = row + 1   
    
    col = 0
    while col < rum_num:
        col = col + 1
        if col == row :
            print(" ", end="")
        else:
            print("*", end="")
    print()
