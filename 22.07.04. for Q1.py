num = int(input("양의 정수를 입력하세요"))

for row in range(1, num+1):
    
    for col in range(1, num+1):
        if col <= row:
            print(col, " ", end="")
        else:
            print(" ", end="")
    print()