num = int(input("양의 정수를 입력하세요"))

row = 0
while row <= num - 1:
    row = row + 1
    
    col = 0
    while col <= num - 1:
        col = col + 1
        if col <= row:
            print(col, end="")
        else:
            print(" ", end="")
        
    print()